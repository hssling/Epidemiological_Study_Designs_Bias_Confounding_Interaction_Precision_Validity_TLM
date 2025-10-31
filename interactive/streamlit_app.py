import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Set page configuration
st.set_page_config(
    page_title="Epidemiology Learning Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        border-left: 4px solid #3498db;
        margin-bottom: 1rem;
    }
    .module-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    .module-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .status-completed {
        background-color: #d4edda;
        color: #155724;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .status-in-progress {
        background-color: #fff3cd;
        color: #856404;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .status-not-started {
        background-color: #f8f9fa;
        color: #6c757d;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for user progress
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        'modules_completed': 2,
        'total_score': 87,
        'study_hours': 4.5,
        'certification_progress': 35,
        'overall_progress': 28,
        'module_statuses': {
            'quiz': 'completed',
            'design_selector': 'completed',
            'bias_simulation': 'in-progress',
            'confounding_explorer': 'not-started',
            'case_study': 'not-started',
            'validity_lab': 'not-started'
        },
        'recent_activities': [
            {'activity': 'Completed Study Design Quiz', 'time': '2 hours ago', 'icon': '📚'},
            {'activity': 'Started Bias Simulation', 'time': '4 hours ago', 'icon': '🎯'},
            {'activity': 'Finished Design Selector', 'time': '1 day ago', 'icon': '🌳'},
            {'activity': 'Reviewed Main Content', 'time': '2 days ago', 'icon': '📖'}
        ]
    }

# Module data
modules_data = {
    'quiz': {
        'title': 'Study Design Quiz',
        'description': 'Test your knowledge of epidemiological study designs',
        'duration': '15 min',
        'icon': '📚',
        'difficulty': 'Beginner'
    },
    'design_selector': {
        'title': 'Study Design Selector',
        'description': 'Interactive decision tree for study design selection',
        'duration': '20 min',
        'icon': '🌳',
        'difficulty': 'Intermediate'
    },
    'bias_simulation': {
        'title': 'Bias Simulation',
        'description': 'Experience how different biases affect study results',
        'duration': '25 min',
        'icon': '🎯',
        'difficulty': 'Intermediate'
    },
    'confounding_explorer': {
        'title': 'Confounding Explorer',
        'description': 'Interactive tool for understanding confounding variables',
        'duration': '30 min',
        'icon': '🔗',
        'difficulty': 'Advanced'
    },
    'case_study': {
        'title': 'Case Study Analysis',
        'description': 'Real-world outbreak investigation simulation',
        'duration': '35 min',
        'icon': '📊',
        'difficulty': 'Advanced'
    },
    'validity_lab': {
        'title': 'Validity & Precision Lab',
        'description': 'Explore measurement concepts through simulations',
        'duration': '25 min',
        'icon': '📈',
        'difficulty': 'Intermediate'
    }
}

def main():
    # Sidebar navigation
    st.sidebar.title("📊 Navigation")
    page = st.sidebar.radio("Go to:", [
        "Dashboard Overview",
        "Module Progress",
        "Interactive Modules",
        "Data Analytics",
        "Settings"
    ])

    if page == "Dashboard Overview":
        show_dashboard_overview()
    elif page == "Module Progress":
        show_module_progress()
    elif page == "Interactive Modules":
        show_interactive_modules()
    elif page == "Data Analytics":
        show_data_analytics()
    elif page == "Settings":
        show_settings()

def show_dashboard_overview():
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>📊 Epidemiology Learning Dashboard</h1>
        <p>Track your progress and master epidemiological study designs</p>
        <p style="font-size: 0.9em; opacity: 0.8; margin-top: 10px;">Created by: Dr. Siddalingaiah H S, Professor, Community Medicine, SIMSRH, Tumkur</p>
    </div>
    """, unsafe_allow_html=True)

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>{st.session_state.user_progress['modules_completed']}</h3>
            <p>Modules Completed</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>{st.session_state.user_progress['total_score']}</h3>
            <p>Total Score</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>{st.session_state.user_progress['study_hours']:.1f}</h3>
            <p>Study Hours</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>{st.session_state.user_progress['certification_progress']}%</h3>
            <p>Certification Progress</p>
        </div>
        """, unsafe_allow_html=True)

    # Progress visualization
    st.subheader("📈 Learning Progress")

    col1, col2 = st.columns([1, 2])

    with col1:
        # Progress circle
        progress = st.session_state.user_progress['overall_progress']
        fig = go.Figure(go.Pie(
            values=[progress, 100-progress],
            hole=0.7,
            marker_colors=['#3498db', '#ecf0f1'],
            textinfo='none'
        ))
        fig.update_layout(
            annotations=[dict(text=f"{progress}%", x=0.5, y=0.5, font_size=30, showarrow=False)],
            showlegend=False,
            width=250,
            height=250
        )
        st.plotly_chart(fig)

    with col2:
        # Recent activities
        st.subheader("Recent Activity")
        for activity in st.session_state.user_progress['recent_activities'][:4]:
            st.markdown(f"""
            <div style="display: flex; align-items: center; padding: 10px 0; border-bottom: 1px solid #eee;">
                <span style="font-size: 1.5em; margin-right: 10px;">{activity['icon']}</span>
                <div>
                    <div style="font-weight: bold;">{activity['activity']}</div>
                    <div style="color: #666; font-size: 0.9em;">{activity['time']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Quick actions
    st.subheader("⚡ Quick Actions")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📚 Start Next Module", key="next_module"):
            st.success("Navigate to the Interactive Modules section below to access Bias Simulation")

    with col2:
        if st.button("📖 Review Content", key="review_content"):
            st.info("Opening main content...")
            st.markdown("[Open Main Content](../content/README.md)")

    with col3:
        if st.button("📊 View Analytics", key="view_analytics"):
            st.info("Loading analytics dashboard...")

    with col4:
        if st.button("🎯 Take Quiz", key="take_quiz"):
            st.info("Navigate to the Interactive Modules section below to access the Study Design Quiz")

def show_module_progress():
    st.header("📚 Module Progress")

    # Progress overview
    progress_data = []
    for module_key, status in st.session_state.user_progress['module_statuses'].items():
        module_info = modules_data[module_key]
        progress_data.append({
            'Module': module_info['title'],
            'Status': status.replace('-', ' ').title(),
            'Duration': module_info['duration'],
            'Difficulty': module_info['difficulty'],
            'Icon': module_info['icon']
        })

    df = pd.DataFrame(progress_data)

    # Status distribution
    status_counts = df['Status'].value_counts()
    fig = px.pie(
        values=status_counts.values,
        names=status_counts.index,
        title="Module Completion Status",
        color_discrete_sequence=['#27ae60', '#f39c12', '#95a5a6']
    )
    st.plotly_chart(fig)

    # Module cards
    st.subheader("Module Details")
    for idx, row in df.iterrows():
        status_class = f"status-{row['Status'].lower().replace(' ', '-')}"
        st.markdown(f"""
        <div class="module-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{row['Icon']} {row['Module']}</h4>
                <span class="{status_class}">{row['Status']}</span>
            </div>
            <p>{modules_data[list(modules_data.keys())[idx]]['description']}</p>
            <div style="display: flex; justify-content: space-between; color: #666; font-size: 0.9em;">
                <span>Duration: {row['Duration']}</span>
                <span>Difficulty: {row['Difficulty']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_interactive_modules():
    st.header("🎓 Interactive Learning Modules")

    # Module filter
    col1, col2 = st.columns([1, 3])
    with col1:
        status_filter = st.selectbox("Filter by Status:",
                                   ["All", "Completed", "In Progress", "Not Started"])

    # Display modules
    for module_key, module_info in modules_data.items():
        status = st.session_state.user_progress['module_statuses'][module_key]

        if status_filter == "All" or status_filter.lower().replace(" ", "-") == status:
            status_class = f"status-{status}"

            with st.container():
                col1, col2, col3 = st.columns([1, 3, 1])

                with col1:
                    st.markdown(f"<h1 style='text-align: center;'>{module_info['icon']}</h1>", unsafe_allow_html=True)

                with col2:
                    st.subheader(module_info['title'])
                    st.write(module_info['description'])
                    st.caption(f"Duration: {module_info['duration']} | Difficulty: {module_info['difficulty']}")

                with col3:
                    st.markdown(f"<div class='{status_class}' style='text-align: center; margin-top: 20px;'>{status.replace('-', ' ').title()}</div>", unsafe_allow_html=True)

                    if st.button(f"Open {module_info['title']}", key=f"open_{module_key}"):
                        st.success(f"Opening {module_info['title']}...")
                        st.markdown(f"[Click here to open]({module_key}.html)")

                st.divider()

def show_data_analytics():
    st.header("📊 Learning Analytics")

    # Generate sample learning data
    dates = pd.date_range(start='2025-10-01', end='2025-10-31', freq='D')
    study_hours = np.random.exponential(1.5, len(dates))
    study_hours = np.clip(study_hours, 0, 4)  # Cap at 4 hours per day

    df_study = pd.DataFrame({
        'Date': dates,
        'Study Hours': study_hours,
        'Modules Completed': np.cumsum(np.random.choice([0, 1], len(dates), p=[0.8, 0.2]))
    })

    # Study hours over time
    fig1 = px.line(df_study, x='Date', y='Study Hours',
                   title='Daily Study Hours',
                   labels={'Study Hours': 'Hours', 'Date': 'Date'})
    st.plotly_chart(fig1)

    # Module completion progress
    fig2 = px.bar(df_study, x='Date', y='Modules Completed',
                  title='Cumulative Module Completion',
                  labels={'Modules Completed': 'Modules Completed', 'Date': 'Date'})
    st.plotly_chart(fig2)

    # Performance by module type
    module_performance = pd.DataFrame({
        'Module Type': ['Knowledge', 'Application', 'Analysis', 'Synthesis'],
        'Average Score': [85, 78, 82, 75],
        'Time Spent (min)': [45, 60, 75, 90]
    })

    fig3 = px.scatter(module_performance, x='Time Spent (min)', y='Average Score',
                     size='Average Score', color='Module Type',
                     title='Performance vs Time Investment')
    st.plotly_chart(fig3)

    # Learning objectives completion
    objectives = pd.DataFrame({
        'Objective': ['Study Design Knowledge', 'Bias Understanding', 'Confounding Analysis',
                     'Validity Concepts', 'Critical Appraisal', 'Research Ethics'],
        'Completion %': [95, 78, 65, 82, 70, 88]
    })

    fig4 = px.bar(objectives, x='Completion %', y='Objective', orientation='h',
                  title='Learning Objectives Progress',
                  labels={'Completion %': 'Completion Percentage'})
    st.plotly_chart(fig4)

def show_settings():
    st.header("⚙️ Settings")

    st.subheader("Learning Preferences")
    col1, col2 = st.columns(2)

    with col1:
        difficulty = st.selectbox("Preferred Difficulty Level:",
                                ["Beginner", "Intermediate", "Advanced"])
        notifications = st.checkbox("Enable Progress Notifications", value=True)

    with col2:
        theme = st.selectbox("Dashboard Theme:",
                           ["Light", "Dark", "Auto"])
        language = st.selectbox("Language:",
                              ["English", "Spanish", "French"])

    st.subheader("Progress Reset")
    if st.button("Reset All Progress", type="secondary"):
        if st.checkbox("Are you sure? This will reset all your learning progress."):
            # Reset progress
            st.session_state.user_progress = {
                'modules_completed': 0,
                'total_score': 0,
                'study_hours': 0,
                'certification_progress': 0,
                'overall_progress': 0,
                'module_statuses': {k: 'not-started' for k in modules_data.keys()},
                'recent_activities': []
            }
            st.success("Progress has been reset!")

    st.subheader("Data Export")
    if st.button("Export Learning Data"):
        # Create sample data for export
        export_data = {
            'progress': st.session_state.user_progress,
            'modules': modules_data,
            'export_date': datetime.now().isoformat()
        }
        st.json(export_data)
        st.download_button(
            label="Download as JSON",
            data=str(export_data),
            file_name="epidemiology_learning_data.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()
