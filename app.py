import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import io

def load_data():
    """Load and process the uploaded Excel files"""
    st.header("Upload Excel Files")
    
    kharif_file = st.file_uploader("Upload Kharif 25 Excel File", type=['xlsx', 'xls'])
    water_level_file = st.file_uploader("Upload Water Level Measurement Excel File", type=['xlsx', 'xls'])
    
    if kharif_file is not None and water_level_file is not None:
        try:
            # Read Kharif data
            kharif_df = pd.read_excel(kharif_file)
            
            # Read water level data
            water_df = pd.read_excel(water_level_file)
            
            return kharif_df, water_df
        except Exception as e:
            st.error(f"Error reading files: {str(e)}")
            return None, None
    
    return None, None

def process_kharif_data(kharif_df):
    """Process Kharif data and extract required columns"""
    
    # Define the columns we need from Kharif data
    required_cols = [
        'Kharif 25 Farm ID',
        'Kharif 25 Village',
        'Kharif 25 Acres farm - farmer reporting',
        'Kharif 25 Paddy transplanting date (TPR)',
        'Kharif 25 - TPR Group Study (Y/N)',
        'Kharif 25 - DSR farm Study (Y/N)',
        'Kharif 25 - Remote Controllers study (Y/N)',
        'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
        'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
        'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
        'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
        'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
        'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)',
        'Kharif 25 - AWD Study (Y/N)',
        'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
        'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
        'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
        'Kharif 25 - AWD Study - Group B -training only (Y/N)',
        'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
        'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
        'Kharif 25 - AWD Study - Group C - Control (Y/N)',
        'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
        'Kharif 25 - AWD Study - Group C - non-complied (Y/N)',
        'Kharif 25 PVC Pipe code - 1',
        'Kharif 25 PVC Pipe code - 2',
        'Kharif 25 PVC Pipe code - 3',
        'Kharif 25 PVC Pipe code - 4',
        'Kharif 25 PVC Pipe code - 5'
    ]
    
    # Check which columns exist in the dataframe
    available_cols = [col for col in required_cols if col in kharif_df.columns]
    missing_cols = [col for col in required_cols if col not in kharif_df.columns]
    
    if missing_cols:
        st.warning(f"Missing columns in Kharif data: {missing_cols}")
    
    # Extract available columns
    processed_kharif = kharif_df[available_cols].copy()
    
    # Handle missing TPR dates - set to June 1, 2025 if empty
    tpr_date_col = 'Kharif 25 Paddy transplanting date (TPR)'
    if tpr_date_col in processed_kharif.columns:
        processed_kharif[tpr_date_col] = processed_kharif[tpr_date_col].fillna('2025-06-01')
        # Convert to datetime if possible
        try:
            processed_kharif[tpr_date_col] = pd.to_datetime(processed_kharif[tpr_date_col], errors='coerce')
            processed_kharif[tpr_date_col] = processed_kharif[tpr_date_col].fillna(pd.to_datetime('2025-06-01'))
        except:
            pass
    
    return processed_kharif

def process_water_data(water_df):
    """Process water level data and extract required columns"""
    
    required_water_cols = [
        'Date',
        'Farm ID',
        'Pipe code ID of the farm',
        'Measure water level inside the PVC pipe - millimeter mm'
    ]
    
    # Check which columns exist
    available_cols = [col for col in required_water_cols if col in water_df.columns]
    missing_cols = [col for col in required_water_cols if col not in water_df.columns]
    
    if missing_cols:
        st.warning(f"Missing columns in water level data: {missing_cols}")
    
    processed_water = water_df[available_cols].copy()
    
    # Convert Date column to datetime if possible
    if 'Date' in processed_water.columns:
        try:
            processed_water['Date'] = pd.to_datetime(processed_water['Date'], errors='coerce')
        except:
            pass
    
    return processed_water

def create_farm_groups(kharif_df):
    """Create farm groups based on specified criteria"""
    
    groups = {}
    
    # Village groups
    if 'Kharif 25 Village' in kharif_df.columns:
        village_groups = kharif_df.groupby('Kharif 25 Village')
        for village, group in village_groups:
            groups[f'Village_{village}'] = group
    
    # Remote Controllers Group A Treatment
    rc_group_a_col = 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)'
    if rc_group_a_col in kharif_df.columns:
        rc_group_a = kharif_df[kharif_df[rc_group_a_col] == 1]
        if not rc_group_a.empty:
            groups['Remote_Controllers_Group_A_Treatment'] = rc_group_a
    
    # Remote Controllers Group B Control
    rc_group_b_col = 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)'
    if rc_group_b_col in kharif_df.columns:
        rc_group_b = kharif_df[kharif_df[rc_group_b_col] == 1]
        if not rc_group_b.empty:
            groups['Remote_Controllers_Group_B_Control'] = rc_group_b
    
    # AWD Study Groups
    awd_groups = ['A', 'B', 'C']
    for group_letter in awd_groups:
        complied_col = f'Kharif 25 - AWD Study - Group {group_letter} - Complied (Y/N)'
        if group_letter == 'A':
            complied_col = 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'
        elif group_letter == 'C':
            complied_col = 'Kharif 25 - AWD Study - Group C - Complied (Y/N)'
        
        if complied_col in kharif_df.columns:
            awd_group = kharif_df[kharif_df[complied_col] == 1]
            if not awd_group.empty:
                groups[f'AWD_Study_Group_{group_letter}_Complied'] = awd_group
    
    # DSR Group
    dsr_col = 'Kharif 25 - DSR farm Study (Y/N)'
    if dsr_col in kharif_df.columns:
        dsr_group = kharif_df[kharif_df[dsr_col] == 1]
        if not dsr_group.empty:
            groups['DSR_Group'] = dsr_group
    
    # TPR Group
    tpr_col = 'Kharif 25 - TPR Group Study (Y/N)'
    if tpr_col in kharif_df.columns:
        tpr_group = kharif_df[kharif_df[tpr_col] == 1]
        if not tpr_group.empty:
            groups['TPR_Group'] = tpr_group
    
    return groups

def merge_data_for_group(kharif_group, water_df, group_name):
    """Merge Kharif and water data for a specific group"""
    
    merged_data = []
    
    for _, farm_row in kharif_group.iterrows():
        farm_id = farm_row.get('Kharif 25 Farm ID', '')
        tpr_date = farm_row.get('Kharif 25 Paddy transplanting date (TPR)', '2025-06-01')
        
        # Get all pipe codes for this farm
        pipe_codes = []
        for i in range(1, 6):
            pipe_col = f'Kharif 25 PVC Pipe code - {i}'
            if pipe_col in farm_row.index and pd.notna(farm_row[pipe_col]):
                pipe_codes.append(farm_row[pipe_col])
        
        # Match with water level data
        farm_water_data = water_df[water_df['Farm ID'] == farm_id]
        
        for _, water_row in farm_water_data.iterrows():
            pipe_code = water_row.get('Pipe code ID of the farm', '')
            
            # Check if this pipe code belongs to this farm
            if pipe_code in pipe_codes or not pipe_codes:  # Include if pipe code matches or no pipe codes available
                merged_row = {
                    'Group': group_name,
                    'Kharif 25 Farm ID': farm_id,
                    'Date': water_row.get('Date', ''),
                    'Pipe code ID of the farm': pipe_code,
                    'Measure water level inside the PVC pipe - millimeter mm': water_row.get('Measure water level inside the PVC pipe - millimeter mm', ''),
                    'Kharif 25 Paddy transplanting date (TPR)': tpr_date
                }
                merged_data.append(merged_row)
    
    return pd.DataFrame(merged_data)

def preprocess_for_visualization(kharif_df, water_df):
    """Preprocess data specifically for visualization"""
    # Select relevant columns
    kharif_cols = [
        "Kharif 25 Farm ID",
        "Kharif 25 Paddy transplanting date (TPR)",
        "Kharif 25 PVC Pipe code - 1",
        "Kharif 25 PVC Pipe code - 2",
        "Kharif 25 PVC Pipe code - 3",
        "Kharif 25 PVC Pipe code - 4",
        "Kharif 25 PVC Pipe code - 5"
    ]
    kharif_subset = kharif_df[kharif_cols].copy()

    # Fill missing TPR with June 1, 2025
    kharif_subset["Kharif 25 Paddy transplanting date (TPR)"] = kharif_subset["Kharif 25 Paddy transplanting date (TPR)"].fillna(pd.Timestamp("2025-06-01"))

    # Filter water monitoring relevant cols
    water_subset = water_df[[
        "Date",
        "Farm ID",
        "Pipe code ID of the farm",
        "Measure water level inside the PVC pipe - millimeter mm"
    ]].copy()

    # Merge on Farm ID
    merged_df = pd.merge(
        water_subset,
        kharif_subset,
        how="left",
        left_on="Farm ID",
        right_on="Kharif 25 Farm ID"
    )

    # Rename columns
    merged_df.rename(columns={
        "Measure water level inside the PVC pipe - millimeter mm": "Water Level (mm)",
        "Kharif 25 Paddy transplanting date (TPR)": "TPR"
    }, inplace=True)

    # Convert date fields
    merged_df["Date"] = pd.to_datetime(merged_df["Date"])
    merged_df["TPR"] = pd.to_datetime(merged_df["TPR"])

    # Calculate days and weeks from TPR
    merged_df["Days from TPR"] = (merged_df["Date"] - merged_df["TPR"]).dt.days
    merged_df["Week from TPR"] = (merged_df["Days from TPR"] // 7).astype(int)

    # Farm-level daily averages
    farm_daily_avg = merged_df.groupby(["Farm ID", "Date"]).agg({
        "Water Level (mm)": "mean",
        "TPR": "first"
    }).reset_index()
    farm_daily_avg["Days from TPR"] = (farm_daily_avg["Date"] - farm_daily_avg["TPR"]).dt.days
    farm_daily_avg["Week from TPR"] = (farm_daily_avg["Days from TPR"] // 7).astype(int)

    # Weekly averages per pipe
    pipe_weekly_avg = merged_df.groupby(["Farm ID", "Pipe code ID of the farm", "Week from TPR"]).agg({
        "Water Level (mm)": "mean"
    }).reset_index().rename(columns={"Water Level (mm)": "Weekly Avg (mm)"})

    # Weekly averages per farm
    farm_weekly_avg = farm_daily_avg.groupby(["Farm ID", "Week from TPR"]).agg({
        "Water Level (mm)": "mean"
    }).reset_index().rename(columns={"Water Level (mm)": "Farm Weekly Avg (mm)"})

    return merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg

def render_visualization_section(kharif_df, water_df, merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg):
    """Render the visualization section of the dashboard"""
    
    st.header("📊 Data Visualization & Analysis")
    
    # Select Farm ID
    farm_ids = sorted(merged_df["Farm ID"].dropna().unique())
    if not farm_ids:
        st.warning("No farm data available for visualization.")
        return
        
    selected_farm = st.selectbox("Select Farm ID for Visualization", farm_ids)

    # Get pipes available for the selected farm from kharif_df
    farm_pipes = kharif_df[kharif_df["Kharif 25 Farm ID"] == selected_farm][[
        "Kharif 25 PVC Pipe code - 1",
        "Kharif 25 PVC Pipe code - 2",
        "Kharif 25 PVC Pipe code - 3",
        "Kharif 25 PVC Pipe code - 4",
        "Kharif 25 PVC Pipe code - 5"
    ]].values.flatten()
    # Remove NaNs and duplicates, convert to list of strings
    farm_pipes = [str(p) for p in farm_pipes if pd.notna(p)]
    farm_pipes = sorted(list(set(farm_pipes)))

    if not farm_pipes:
        st.warning(f"No pipe codes found for Farm ID: {selected_farm}")
        return

    # Pipe selection option
    selected_pipes = st.multiselect(
        "Select Pipe(s) to visualize (from selected farm)",
        options=farm_pipes,
        default=farm_pipes  # default all selected
    )

    if not selected_pipes:
        st.warning("Please select at least one pipe to visualize.")
        return

    # Filter merged_df for selected farm and pipes
    filtered_df = merged_df[
        (merged_df["Farm ID"] == selected_farm) &
        (merged_df["Pipe code ID of the farm"].astype(str).isin(selected_pipes))
    ]

    # Farm daily avg filtered for selected farm
    farm_daily_filt = farm_daily_avg[farm_daily_avg["Farm ID"] == selected_farm]

    # Pipe weekly avg filtered for selected farm and selected pipes
    pipe_weekly_filt = pipe_weekly_avg[
        (pipe_weekly_avg["Farm ID"] == selected_farm) &
        (pipe_weekly_avg["Pipe code ID of the farm"].astype(str).isin(selected_pipes))
    ]

    # Farm weekly avg filtered for selected farm
    farm_weekly_filt = farm_weekly_avg[farm_weekly_avg["Farm ID"] == selected_farm]

    st.markdown(f"### Visualizations for Farm ID: {selected_farm}")

    # -------- Graph 1: Individual Farm Water Levels Daily --------
    st.markdown("#### Graph 1: Daily Water Levels per Pipe + Farm Average")

    fig1 = go.Figure()

    # Plot each selected pipe daily water level
    for pipe in selected_pipes:
        pipe_df = filtered_df[filtered_df["Pipe code ID of the farm"].astype(str) == pipe]
        pipe_df = pipe_df.sort_values("Days from TPR")
        fig1.add_trace(go.Scatter(
            x=pipe_df["Days from TPR"],
            y=pipe_df["Water Level (mm)"],
            mode='lines+markers',
            name=f"Pipe {pipe}"
        ))

    # Plot farm average daily water level line
    farm_daily_filt_sorted = farm_daily_filt.sort_values("Days from TPR")
    fig1.add_trace(go.Scatter(
        x=farm_daily_filt_sorted["Days from TPR"],
        y=farm_daily_filt_sorted["Water Level (mm)"],
        mode='lines+markers',
        name="Farm Average",
        line=dict(width=4, dash='dash'),
        marker=dict(symbol='star', size=10)
    ))

    fig1.update_layout(
        xaxis_title="Days from Transplanting",
        yaxis_title="PVC Water Level (mm)",
        legend_title="Legend",
        hovermode="x unified"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # -------- Graph 2: Weekly Water Level Trends --------
    st.markdown("#### Graph 2: Weekly Water Level Trends per Pipe + Farm Average")

    fig2 = go.Figure()

    # Plot weekly avg per pipe
    for pipe in selected_pipes:
        pipe_wk_df = pipe_weekly_filt[pipe_weekly_filt["Pipe code ID of the farm"].astype(str) == pipe]
        pipe_wk_df = pipe_wk_df.sort_values("Week from TPR")
        fig2.add_trace(go.Scatter(
            x=pipe_wk_df["Week from TPR"],
            y=pipe_wk_df["Weekly Avg (mm)"],
            mode='lines+markers',
            name=f"Pipe {pipe}"
        ))

    # Plot farm weekly average
    farm_weekly_filt_sorted = farm_weekly_filt.sort_values("Week from TPR")
    fig2.add_trace(go.Scatter(
        x=farm_weekly_filt_sorted["Week from TPR"],
        y=farm_weekly_filt_sorted["Farm Weekly Avg (mm)"],
        mode='lines+markers',
        name="Farm Weekly Average",
        line=dict(width=4, dash='dash'),
        marker=dict(symbol='star', size=10)
    ))

    fig2.update_layout(
        xaxis_title="Weeks from Transplanting",
        yaxis_title="PVC Water Level (mm)",
        legend_title="Legend",
        hovermode="x unified"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # -------- Table 1: Days from TPR vs Water Levels of All Farms --------
    st.markdown("### Table 1: Days from Transplanting vs Water Level per Farm")

    # Prepare table data for Table 1:
    # Pivot farm_daily_avg data to have Days from TPR as rows, Farms as columns
    farm_water_pivot = farm_daily_avg.pivot_table(
        index="Days from TPR",
        columns="Farm ID",
        values="Water Level (mm)"
    )

    farm_water_pivot.index.name = "Days from Transplanting"
    farm_water_pivot = farm_water_pivot.reset_index()

    st.dataframe(farm_water_pivot.style.format(precision=2))

    # -------- Table 2: Days from TPR vs Water Levels of Pipes for Selected Farm --------
    st.markdown(f"### Table 2: Days from Transplanting vs Water Level per Pipe (Farm ID: {selected_farm})")

    # Prepare table data for Table 2:
    # Filter merged_df for selected farm and pipes
    pipe_daily_df = merged_df[
        (merged_df["Farm ID"] == selected_farm) &
        (merged_df["Pipe code ID of the farm"].astype(str).isin(selected_pipes))
    ]

    # Pivot so that index is Days from TPR and columns are Pipe IDs
    pipe_water_pivot = pipe_daily_df.pivot_table(
        index="Days from TPR",
        columns="Pipe code ID of the farm",
        values="Water Level (mm)"
    )

    pipe_water_pivot.index.name = "Days from Transplanting"
    pipe_water_pivot = pipe_water_pivot.reset_index()

    st.dataframe(pipe_water_pivot.style.format(precision=2))

def render_group_analysis_section(processed_kharif, processed_water):
    """Render the group analysis section of the dashboard"""
    
    st.header("📋 Group Analysis & Data Export")
    
    # Create groups
    farm_groups = create_farm_groups(processed_kharif)
    
    # Create merged datasets
    merged_datasets = {}
    
    # Overall dataset
    overall_merged = merge_data_for_group(processed_kharif, processed_water, 'Overall')
    merged_datasets['Overall'] = overall_merged
    
    # Group-specific datasets
    for group_name, group_df in farm_groups.items():
        group_merged = merge_data_for_group(group_df, processed_water, group_name)
        merged_datasets[group_name] = group_merged
    
    # Display results
    st.subheader("Analysis Results")
    
    selected_group = st.selectbox("Select Group to View", list(merged_datasets.keys()))
    
    if selected_group in merged_datasets:
        group_data = merged_datasets[selected_group]
        
        st.write(f"**{selected_group}** - {len(group_data)} records")
        
        if not group_data.empty:
            st.dataframe(group_data)
            
            # Summary statistics
            st.subheader("Summary Statistics")
            if 'Measure water level inside the PVC pipe - millimeter mm' in group_data.columns:
                water_levels = pd.to_numeric(group_data['Measure water level inside the PVC pipe - millimeter mm'], errors='coerce')
                water_levels = water_levels.dropna()
                
                if not water_levels.empty:
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Mean Water Level (mm)", f"{water_levels.mean():.2f}")
                    with col2:
                        st.metric("Median Water Level (mm)", f"{water_levels.median():.2f}")
                    with col3:
                        st.metric("Min Water Level (mm)", f"{water_levels.min():.2f}")
                    with col4:
                        st.metric("Max Water Level (mm)", f"{water_levels.max():.2f}")
            
            # Download option
            csv_buffer = io.StringIO()
            group_data.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
            
            st.download_button(
                label=f"Download {selected_group} Data as CSV",
                data=csv_data,
                file_name=f"farm_data_{selected_group.lower().replace(' ', '_')}.csv",
                mime="text/csv"
            )
        else:
            st.warning(f"No data found for {selected_group}")
    
    # Download all datasets
    st.subheader("Download All Datasets")
    
    if st.button("Generate All CSV Files"):
        # Create a simple method to combine all CSVs into one download
        all_data = []
        for group_name, group_data in merged_datasets.items():
            if not group_data.empty:
                all_data.append(group_data)
        
        if all_data:
            combined_data = pd.concat(all_data, ignore_index=True)
            csv_buffer = io.StringIO()
            combined_data.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
            
            st.download_button(
                label="Download Combined Data as CSV",
                data=csv_data,
                file_name="all_farm_data_combined.csv",
                mime="text/csv"
            )
    
    # Display group summary
    st.subheader("Group Summary")
    summary_data = []
    for group_name, group_data in merged_datasets.items():
        if not group_data.empty:
            unique_farms = group_data['Kharif 25 Farm ID'].nunique()
            total_records = len(group_data)
            
            # Calculate water level stats if available
            water_levels = pd.to_numeric(group_data['Measure water level inside the PVC pipe - millimeter mm'], errors='coerce')
            water_levels = water_levels.dropna()
            avg_water_level = water_levels.mean() if not water_levels.empty else 0
            
            summary_data.append({
                'Group': group_name,
                'Unique Farms': unique_farms,
                'Total Records': total_records,
                'Avg Water Level (mm)': round(avg_water_level, 2) if avg_water_level > 0 else 'N/A'
            })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df)

# def main():
#     st.set_page_config(
#         page_title="Agricultural Data Analysis Dashboard",
#         page_icon="🌾",
#         layout="wide"
#     )
    
#     st.title("🌾 Agricultural Data Analysis Dashboard")
#     st.markdown("**Comprehensive analysis of Kharif 25 farm data with water level measurements**")
    
#     # Load data
#     kharif_df, water_df = load_data()
    

def main():
    st.set_page_config(
        page_title="Agricultural Data Analysis Dashboard",
        page_icon="🌾",
        layout="wide"
    )
    
    st.title("Agricultural Data Analysis Dashboard")
    # st.markdown("**Comprehensive analysis of Kharif 25 farm data with water level measurements**")
    
    # Add button for 2024 data analysis
    # st.markdown("---")
    # st.markdown("### Looking for previous year's data?")
    st.link_button("Analyze 2024 Data", "https://v45bgthcmmrztmbstkddra.streamlit.app/")
    # st.markdown("---")
    
    # Load data
    kharif_df, water_df = load_data()

    if kharif_df is not None and water_df is not None:
        st.success("✅ Files loaded successfully!")
        
        # Show data info in sidebar
        with st.sidebar:
            st.subheader("📊 Data Overview")
            st.write(f"**Kharif Data:**")
            st.write(f"• Rows: {len(kharif_df):,}")
            st.write(f"• Columns: {len(kharif_df.columns)}")
            st.write(f"**Water Level Data:**")
            st.write(f"• Rows: {len(water_df):,}")
            st.write(f"• Columns: {len(water_df.columns)}")
        
        # Process data
        with st.spinner("Processing data..."):
            processed_kharif = process_kharif_data(kharif_df)
            processed_water = process_water_data(water_df)
            
            # Preprocess for visualization
            merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg = preprocess_for_visualization(kharif_df, water_df)
        
        # Create tabs for different sections
        tab1, tab2 = st.tabs(["📊 Visualization & Analysis", "📋 Group Analysis & Export"])
        
        with tab1:
            render_visualization_section(kharif_df, water_df, merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg)
        
        with tab2:
            render_group_analysis_section(processed_kharif, processed_water)
    
    else:
        st.info("📁 Please upload both Kharif Excel and Water Level Measurement Excel files to proceed.")
        
        # Show example data structure
        with st.expander("ℹ️ Expected Data Structure"):
            st.markdown("""
            **Kharif 25 Excel File should contain:**
            - Kharif 25 Farm ID
            - Kharif 25 Village
            - Kharif 25 Paddy transplanting date (TPR)
            - Various study group columns (TPR, DSR, Remote Controllers, AWD)
            - PVC Pipe codes (1-5)
            
            **Water Level Measurement Excel File should contain:**
            - Date
            - Farm ID
            - Pipe code ID of the farm
            - Measure water level inside the PVC pipe - millimeter mm
            """)

if __name__ == "__main__":
    main()
