# # # import streamlit as st
# # # import pandas as pd
# # # import numpy as np
# # # from datetime import datetime
# # # import plotly.graph_objects as go
# # # import plotly.express as px
# # # import io

# # # def load_data():
# # #     """Load and process the uploaded Excel files"""
# # #     st.header("Upload Excel Files")
    
# # #     kharif_file = st.file_uploader("Upload Kharif 25 Excel File", type=['xlsx', 'xls'])
# # #     water_level_file = st.file_uploader("Upload Water Level Measurement Excel File", type=['xlsx', 'xls'])
    
# # #     if kharif_file is not None and water_level_file is not None:
# # #         try:
# # #             # Read Kharif data
# # #             kharif_df = pd.read_excel(kharif_file)
            
# # #             # Read water level data
# # #             water_df = pd.read_excel(water_level_file)
            
# # #             return kharif_df, water_df
# # #         except Exception as e:
# # #             st.error(f"Error reading files: {str(e)}")
# # #             return None, None
    
# # #     return None, None

# # # def process_kharif_data(kharif_df):
# # #     """Process Kharif data and extract required columns"""
    
# # #     # Define the columns we need from Kharif data
# # #     required_cols = [
# # #         'Kharif 25 Farm ID',
# # #         'Kharif 25 Village',
# # #         'Kharif 25 Acres farm - farmer reporting',
# # #         'Kharif 25 Paddy transplanting date (TPR)',
# # #         'Kharif 25 - TPR Group Study (Y/N)',
# # #         'Kharif 25 - DSR farm Study (Y/N)',
# # #         'Kharif 25 - Remote Controllers study (Y/N)',
# # #         'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
# # #         'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
# # #         'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
# # #         'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
# # #         'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
# # #         'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)',
# # #         'Kharif 25 - AWD Study (Y/N)',
# # #         'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
# # #         'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
# # #         'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
# # #         'Kharif 25 - AWD Study - Group B -training only (Y/N)',
# # #         'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
# # #         'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
# # #         'Kharif 25 - AWD Study - Group C - Control (Y/N)',
# # #         'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
# # #         'Kharif 25 - AWD Study - Group C - non-complied (Y/N)',
# # #         'Kharif 25 PVC Pipe code - 1',
# # #         'Kharif 25 PVC Pipe code - 2',
# # #         'Kharif 25 PVC Pipe code - 3',
# # #         'Kharif 25 PVC Pipe code - 4',
# # #         'Kharif 25 PVC Pipe code - 5'
# # #     ]
    
# # #     # Check which columns exist in the dataframe
# # #     available_cols = [col for col in required_cols if col in kharif_df.columns]
# # #     missing_cols = [col for col in required_cols if col not in kharif_df.columns]
    
# # #     if missing_cols:
# # #         st.warning(f"Missing columns in Kharif data: {missing_cols}")
    
# # #     # Extract available columns
# # #     processed_kharif = kharif_df[available_cols].copy()
    
# # #     # Handle missing TPR dates - set to June 1, 2025 if empty
# # #     tpr_date_col = 'Kharif 25 Paddy transplanting date (TPR)'
# # #     if tpr_date_col in processed_kharif.columns:
# # #         processed_kharif[tpr_date_col] = processed_kharif[tpr_date_col].fillna('2025-06-01')
# # #         # Convert to datetime if possible
# # #         try:
# # #             processed_kharif[tpr_date_col] = pd.to_datetime(processed_kharif[tpr_date_col], errors='coerce')
# # #             processed_kharif[tpr_date_col] = processed_kharif[tpr_date_col].fillna(pd.to_datetime('2025-06-01'))
# # #         except:
# # #             pass
    
# # #     return processed_kharif

# # # def process_water_data(water_df):
# # #     """Process water level data and extract required columns"""
    
# # #     required_water_cols = [
# # #         'Date',
# # #         'Farm ID',
# # #         'Pipe code ID of the farm',
# # #         'Measure water level inside the PVC pipe - millimeter mm'
# # #     ]
    
# # #     # Check which columns exist
# # #     available_cols = [col for col in required_water_cols if col in water_df.columns]
# # #     missing_cols = [col for col in required_water_cols if col not in water_df.columns]
    
# # #     if missing_cols:
# # #         st.warning(f"Missing columns in water level data: {missing_cols}")
    
# # #     processed_water = water_df[available_cols].copy()
    
# # #     # Convert Date column to datetime if possible
# # #     if 'Date' in processed_water.columns:
# # #         try:
# # #             processed_water['Date'] = pd.to_datetime(processed_water['Date'], errors='coerce')
# # #         except:
# # #             pass
    
# # #     return processed_water

# # # def create_farm_groups(kharif_df):
# # #     """Create farm groups based on specified criteria"""
    
# # #     groups = {}
    
# # #     # Village groups
# # #     if 'Kharif 25 Village' in kharif_df.columns:
# # #         village_groups = kharif_df.groupby('Kharif 25 Village')
# # #         for village, group in village_groups:
# # #             groups[f'Village: {village}'] = group
    
# # #     # Remote Controllers Group A Treatment
# # #     rc_group_a_col = 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)'
# # #     if rc_group_a_col in kharif_df.columns:
# # #         rc_group_a = kharif_df[kharif_df[rc_group_a_col] == 1]
# # #         if not rc_group_a.empty:
# # #             groups['Remote Controllers: Group A (Treatment)'] = rc_group_a
    
# # #     # Remote Controllers Group B Control
# # #     rc_group_b_col = 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)'
# # #     if rc_group_b_col in kharif_df.columns:
# # #         rc_group_b = kharif_df[kharif_df[rc_group_b_col] == 1]
# # #         if not rc_group_b.empty:
# # #             groups['Remote Controllers: Group B (Control)'] = rc_group_b
    
# # #     # AWD Study Groups
# # #     awd_groups = ['A', 'B', 'C']
# # #     for group_letter in awd_groups:
# # #         complied_col = f'Kharif 25 - AWD Study - Group {group_letter} - Complied (Y/N)'
# # #         if group_letter == 'A':
# # #             complied_col = 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'
# # #         elif group_letter == 'B':
# # #             complied_col = 'Kharif 25 - AWD Study - Group B - Complied (Y/N)'
# # #         elif group_letter == 'C':
# # #             complied_col = 'Kharif 25 - AWD Study - Group C - Complied (Y/N)'
        
# # #         if complied_col in kharif_df.columns:
# # #             awd_group = kharif_df[kharif_df[complied_col] == 1]
# # #             if not awd_group.empty:
# # #                 groups[f'AWD Study: Group {group_letter} (Complied)'] = awd_group
    
# # #     # DSR Group
# # #     dsr_col = 'Kharif 25 - DSR farm Study (Y/N)'
# # #     if dsr_col in kharif_df.columns:
# # #         dsr_group = kharif_df[kharif_df[dsr_col] == 1]
# # #         if not dsr_group.empty:
# # #             groups['DSR Group'] = dsr_group
    
# # #     # TPR Group
# # #     tpr_col = 'Kharif 25 - TPR Group Study (Y/N)'
# # #     if tpr_col in kharif_df.columns:
# # #         tpr_group = kharif_df[kharif_df[tpr_col] == 1]
# # #         if not tpr_group.empty:
# # #             groups['TPR Group'] = tpr_group
    
# # #     # Add overall group
# # #     groups['All Farms'] = kharif_df
    
# # #     return groups

# # # def preprocess_for_visualization(kharif_df, water_df):
# # #     """Preprocess data specifically for visualization"""
# # #     # Select relevant columns
# # #     kharif_cols = [
# # #         "Kharif 25 Farm ID",
# # #         "Kharif 25 Paddy transplanting date (TPR)",
# # #         "Kharif 25 PVC Pipe code - 1",
# # #         "Kharif 25 PVC Pipe code - 2",
# # #         "Kharif 25 PVC Pipe code - 3",
# # #         "Kharif 25 PVC Pipe code - 4",
# # #         "Kharif 25 PVC Pipe code - 5"
# # #     ]
# # #     kharif_subset = kharif_df[kharif_cols].copy()

# # #     # Fill missing TPR with June 1, 2025
# # #     kharif_subset["Kharif 25 Paddy transplanting date (TPR)"] = kharif_subset["Kharif 25 Paddy transplanting date (TPR)"].fillna(pd.Timestamp("2025-06-01"))

# # #     # Filter water monitoring relevant cols
# # #     water_subset = water_df[[
# # #         "Date",
# # #         "Farm ID",
# # #         "Pipe code ID of the farm",
# # #         "Measure water level inside the PVC pipe - millimeter mm"
# # #     ]].copy()

# # #     # Merge on Farm ID
# # #     merged_df = pd.merge(
# # #         water_subset,
# # #         kharif_subset,
# # #         how="left",
# # #         left_on="Farm ID",
# # #         right_on="Kharif 25 Farm ID"
# # #     )

# # #     # Rename columns
# # #     merged_df.rename(columns={
# # #         "Measure water level inside the PVC pipe - millimeter mm": "Water Level (mm)",
# # #         "Kharif 25 Paddy transplanting date (TPR)": "TPR"
# # #     }, inplace=True)

# # #     # Convert date fields
# # #     merged_df["Date"] = pd.to_datetime(merged_df["Date"])
# # #     merged_df["TPR"] = pd.to_datetime(merged_df["TPR"])

# # #     # Calculate days and weeks from TPR
# # #     merged_df["Days from TPR"] = (merged_df["Date"] - merged_df["TPR"]).dt.days
# # #     merged_df["Week from TPR"] = (merged_df["Days from TPR"] // 7).astype(int)

# # #     # Farm-level daily averages
# # #     farm_daily_avg = merged_df.groupby(["Farm ID", "Date"]).agg({
# # #         "Water Level (mm)": "mean",
# # #         "TPR": "first"
# # #     }).reset_index()
# # #     farm_daily_avg["Days from TPR"] = (farm_daily_avg["Date"] - farm_daily_avg["TPR"]).dt.days
# # #     farm_daily_avg["Week from TPR"] = (farm_daily_avg["Days from TPR"] // 7).astype(int)

# # #     # Weekly averages per pipe
# # #     pipe_weekly_avg = merged_df.groupby(["Farm ID", "Pipe code ID of the farm", "Week from TPR"]).agg({
# # #         "Water Level (mm)": "mean"
# # #     }).reset_index().rename(columns={"Water Level (mm)": "Weekly Avg (mm)"})

# # #     # Weekly averages per farm
# # #     farm_weekly_avg = farm_daily_avg.groupby(["Farm ID", "Week from TPR"]).agg({
# # #         "Water Level (mm)": "mean"
# # #     }).reset_index().rename(columns={"Water Level (mm)": "Farm Weekly Avg (mm)"})

# # #     return merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg

# # # def render_individual_farm_visualization(kharif_df, water_df, merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg):
# # #     """Render individual farm visualization section with marker-only plots"""
# # #     st.header("Individual Farm Visualization")
    
# # #     # Select Farm ID
# # #     farm_ids = sorted(merged_df["Farm ID"].dropna().unique())
# # #     if not farm_ids:
# # #         st.warning("No farm data available for visualization.")
# # #         return
        
# # #     selected_farm = st.selectbox("Select Farm ID", farm_ids)

# # #     # Get pipes available for the selected farm from kharif_df
# # #     farm_pipes = kharif_df[kharif_df["Kharif 25 Farm ID"] == selected_farm][[
# # #         "Kharif 25 PVC Pipe code - 1",
# # #         "Kharif 25 PVC Pipe code - 2",
# # #         "Kharif 25 PVC Pipe code - 3",
# # #         "Kharif 25 PVC Pipe code - 4",
# # #         "Kharif 25 PVC Pipe code - 5"
# # #     ]].values.flatten()
# # #     # Remove NaNs and duplicates, convert to list of strings
# # #     farm_pipes = [str(p) for p in farm_pipes if pd.notna(p)]
# # #     farm_pipes = sorted(list(set(farm_pipes)))

# # #     if not farm_pipes:
# # #         st.warning(f"No pipe codes found for Farm ID: {selected_farm}")
# # #         return

# # #     # Pipe selection option
# # #     selected_pipes = st.multiselect(
# # #         "Select Pipe(s) to visualize",
# # #         options=farm_pipes,
# # #         default=farm_pipes[:2] if len(farm_pipes) > 1 else farm_pipes
# # #     )

# # #     if not selected_pipes:
# # #         st.warning("Please select at least one pipe to visualize.")
# # #         return

# # #     # Filter merged_df for selected farm and pipes
# # #     filtered_df = merged_df[
# # #         (merged_df["Farm ID"] == selected_farm) &
# # #         (merged_df["Pipe code ID of the farm"].astype(str).isin(selected_pipes))
# # #     ]

# # #     # Farm daily avg filtered for selected farm
# # #     farm_daily_filt = farm_daily_avg[farm_daily_avg["Farm ID"] == selected_farm]

# # #     # Pipe weekly avg filtered for selected farm and selected pipes
# # #     pipe_weekly_filt = pipe_weekly_avg[
# # #         (pipe_weekly_avg["Farm ID"] == selected_farm) &
# # #         (pipe_weekly_avg["Pipe code ID of the farm"].astype(str).isin(selected_pipes))
# # #     ]

# # #     # Farm weekly avg filtered for selected farm
# # #     farm_weekly_filt = farm_weekly_avg[farm_weekly_avg["Farm ID"] == selected_farm]

# # #     st.markdown(f"### Farm ID: `{selected_farm}`")

# # #     # -------- Graph 1: Individual Farm Water Levels Daily --------
# # #     st.markdown("#### Daily Water Levels per Pipe + Farm Average")

# # #     fig1 = go.Figure()

# # #     # Plot each selected pipe daily water level as markers only
# # #     for pipe in selected_pipes:
# # #         pipe_df = filtered_df[filtered_df["Pipe code ID of the farm"].astype(str) == pipe]
# # #         pipe_df = pipe_df.sort_values("Days from TPR")
# # #         fig1.add_trace(go.Scatter(
# # #             x=pipe_df["Days from TPR"],
# # #             y=pipe_df["Water Level (mm)"],
# # #             mode='markers',
# # #             name=f"Pipe {pipe}",
# # #             marker=dict(size=8)
# # #         ))

# # #     # Plot farm average daily water level as line + markers
# # #     farm_daily_filt_sorted = farm_daily_filt.sort_values("Days from TPR")
# # #     fig1.add_trace(go.Scatter(
# # #         x=farm_daily_filt_sorted["Days from TPR"],
# # #         y=farm_daily_filt_sorted["Water Level (mm)"],
# # #         mode='lines+markers',
# # #         name="Farm Average",
# # #         line=dict(width=3, color='white'),
# # #         marker=dict(symbol='diamond', size=10, color='white')
# # #     ))

# # #     fig1.update_layout(
# # #         xaxis_title="Days from Transplanting",
# # #         yaxis_title="PVC Water Level (mm)",
# # #         legend_title="Legend",
# # #         hovermode="x unified"
# # #     )
# # #     st.plotly_chart(fig1, use_container_width=True)

# # #     # -------- Graph 2: Weekly Water Level Trends --------
# # #     st.markdown("#### Weekly Water Level Trends per Pipe + Farm Average")

# # #     fig2 = go.Figure()

# # #     # Plot weekly avg per pipe as markers only
# # #     for pipe in selected_pipes:
# # #         pipe_wk_df = pipe_weekly_filt[pipe_weekly_filt["Pipe code ID of the farm"].astype(str) == pipe]
# # #         pipe_wk_df = pipe_wk_df.sort_values("Week from TPR")
# # #         fig2.add_trace(go.Scatter(
# # #             x=pipe_wk_df["Week from TPR"],
# # #             y=pipe_wk_df["Weekly Avg (mm)"],
# # #             mode='markers',
# # #             name=f"Pipe {pipe}",
# # #             marker=dict(size=8)
# # #         ))

# # #     # Plot farm weekly average as line + markers
# # #     farm_weekly_filt_sorted = farm_weekly_filt.sort_values("Week from TPR")
# # #     fig2.add_trace(go.Scatter(
# # #         x=farm_weekly_filt_sorted["Week from TPR"],
# # #         y=farm_weekly_filt_sorted["Farm Weekly Avg (mm)"],
# # #         mode='lines+markers',
# # #         name="Farm Weekly Average",
# # #         line=dict(width=3, color='white'),
# # #         marker=dict(symbol='diamond', size=10, color='white')
# # #     ))

# # #     fig2.update_layout(
# # #         xaxis_title="Weeks from Transplanting",
# # #         yaxis_title="PVC Water Level (mm)",
# # #         legend_title="Legend",
# # #         hovermode="x unified"
# # #     )
# # #     st.plotly_chart(fig2, use_container_width=True)

# # #     # -------- Table 1: Days from TPR vs Water Levels --------
# # #     st.markdown("### Daily Water Levels")

# # #     # Prepare table data
# # #     pipe_daily_df = merged_df[
# # #         (merged_df["Farm ID"] == selected_farm) &
# # #         (merged_df["Pipe code ID of the farm"].astype(str).isin(selected_pipes))
# # #     ]

# # #     # Pivot so that index is Days from TPR and columns are Pipe IDs
# # #     pipe_water_pivot = pipe_daily_df.pivot_table(
# # #         index="Days from TPR",
# # #         columns="Pipe code ID of the farm",
# # #         values="Water Level (mm)",
# # #         aggfunc='mean'
# # #     ).reset_index()

# # #     # Add farm average column
# # #     farm_avg_daily = farm_daily_filt.groupby("Days from TPR")["Water Level (mm)"].mean().reset_index()
# # #     pipe_water_pivot = pd.merge(pipe_water_pivot, farm_avg_daily, on="Days from TPR", how="left")
# # #     pipe_water_pivot = pipe_water_pivot.rename(columns={"Water Level (mm)": "Farm Average"})

# # #     st.dataframe(pipe_water_pivot.style.format(precision=2).set_table_styles([
# # #         {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]}
# # #     ]))

# # # def render_group_visualization(groups, farm_daily_avg, farm_weekly_avg):
# # #     """Render group visualization section with marker-only plots"""
# # #     st.header("Group Visualization")
    
# # #     if not groups:
# # #         st.warning("No groups available for visualization.")
# # #         return
        
# # #     # Select group
# # #     group_names = list(groups.keys())
# # #     selected_group = st.selectbox("Select Group", group_names)
    
# # #     # Get farm IDs in the selected group
# # #     group_df = groups[selected_group]
# # #     group_farm_ids = group_df["Kharif 25 Farm ID"].unique().tolist()
    
# # #     if not group_farm_ids:
# # #         st.warning(f"No farms found in group: {selected_group}")
# # #         return
        
# # #     # Select farms within the group
# # #     selected_farms = st.multiselect(
# # #         "Select Farms to Include",
# # #         options=group_farm_ids,
# # #         default=group_farm_ids[:min(5, len(group_farm_ids))]  # Default to first 5 farms
# # #     )
    
# # #     if not selected_farms:
# # #         st.warning("Please select at least one farm.")
# # #         return
        
# # #     # Filter data for selected farms
# # #     group_daily = farm_daily_avg[farm_daily_avg["Farm ID"].isin(selected_farms)]
# # #     group_weekly = farm_weekly_avg[farm_weekly_avg["Farm ID"].isin(selected_farms)]
    
# # #     # Calculate group averages
# # #     group_daily_avg = group_daily.groupby("Days from TPR").agg({
# # #         "Water Level (mm)": "mean"
# # #     }).reset_index()
# # #     group_daily_avg["Farm ID"] = "Group Average"
    
# # #     group_weekly_avg = group_weekly.groupby("Week from TPR").agg({
# # #         "Farm Weekly Avg (mm)": "mean"
# # #     }).reset_index()
# # #     group_weekly_avg["Farm ID"] = "Group Average"
    
# # #     st.markdown(f"### Group: `{selected_group}` | Farms: `{len(selected_farms)}`")
    
# # #     # -------- Graph 1: Group Daily Water Levels --------
# # #     st.markdown("#### Daily Water Levels per Farm + Group Average")
    
# # #     fig1 = go.Figure()
    
# # #     # Plot each farm as markers only
# # #     for farm_id in selected_farms:
# # #         farm_data = group_daily[group_daily["Farm ID"] == farm_id]
# # #         fig1.add_trace(go.Scatter(
# # #             x=farm_data["Days from TPR"],
# # #             y=farm_data["Water Level (mm)"],
# # #             mode='markers',
# # #             name=farm_id,
# # #             marker=dict(size=6)
# # #         ))
    
# # #     # Add group average as line + markers
# # #     fig1.add_trace(go.Scatter(
# # #         x=group_daily_avg["Days from TPR"],
# # #         y=group_daily_avg["Water Level (mm)"],
# # #         mode='lines+markers',
# # #         name="Group Average",
# # #         line=dict(width=3, dash='solid', color='white'),
# # #         marker=dict(symbol='diamond', size=10)
# # #     ))
    
# # #     fig1.update_layout(
# # #         xaxis_title="Days from Transplanting",
# # #         yaxis_title="PVC Water Level (mm)",
# # #         legend_title="Farm ID",
# # #         hovermode="x unified"
# # #     )
# # #     st.plotly_chart(fig1, use_container_width=True)
    
# # #     # -------- Graph 2: Group Weekly Water Levels --------
# # #     st.markdown("#### Weekly Water Level Trends per Farm + Group Average")
    
# # #     fig2 = go.Figure()
    
# # #     # Plot each farm as markers only
# # #     for farm_id in selected_farms:
# # #         farm_data = group_weekly[group_weekly["Farm ID"] == farm_id]
# # #         fig2.add_trace(go.Scatter(
# # #             x=farm_data["Week from TPR"],
# # #             y=farm_data["Farm Weekly Avg (mm)"],
# # #             mode='markers',
# # #             name=farm_id,
# # #             marker=dict(size=6)
# # #         ))
    
# # #     # Add group average as line + markers
# # #     fig2.add_trace(go.Scatter(
# # #         x=group_weekly_avg["Week from TPR"],
# # #         y=group_weekly_avg["Farm Weekly Avg (mm)"],
# # #         mode='lines+markers',
# # #         name="Group Average",
# # #         line=dict(width=3, dash='solid', color='white'),
# # #         marker=dict(symbol='diamond', size=10)
# # #     ))
    
# # #     fig2.update_layout(
# # #         xaxis_title="Weeks from Transplanting",
# # #         yaxis_title="PVC Water Level (mm)",
# # #         legend_title="Farm ID",
# # #         hovermode="x unified"
# # #     )
# # #     st.plotly_chart(fig2, use_container_width=True)
    
# # #     # -------- Table 1: Group Daily Water Levels --------
# # #     st.markdown("### Daily Water Levels by Farm")
    
# # #     # Pivot data for table
# # #     daily_pivot = group_daily.pivot_table(
# # #         index="Days from TPR",
# # #         columns="Farm ID",
# # #         values="Water Level (mm)",
# # #         aggfunc="mean"
# # #     ).reset_index()
    
# # #     # Add group average column
# # #     daily_pivot = pd.merge(daily_pivot, group_daily_avg[["Days from TPR", "Water Level (mm)"]], 
# # #                           on="Days from TPR", how="left")
# # #     daily_pivot = daily_pivot.rename(columns={"Water Level (mm)": "Group Average"})
    
# # #     st.dataframe(daily_pivot.style.format(precision=2).set_table_styles([
# # #         {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]}
# # #     ]))
    
# # #     # -------- Table 2: Group Weekly Water Levels --------
# # #     st.markdown("### Weekly Water Levels by Farm")
    
# # #     # Pivot data for table
# # #     weekly_pivot = group_weekly.pivot_table(
# # #         index="Week from TPR",
# # #         columns="Farm ID",
# # #         values="Farm Weekly Avg (mm)",
# # #         aggfunc="mean"
# # #     ).reset_index()
    
# # #     # Add group average column
# # #     weekly_pivot = pd.merge(weekly_pivot, group_weekly_avg[["Week from TPR", "Farm Weekly Avg (mm)"]], 
# # #                            on="Week from TPR", how="left")
# # #     weekly_pivot = weekly_pivot.rename(columns={"Farm Weekly Avg (mm)": "Group Average"})
    
# # #     st.dataframe(weekly_pivot.style.format(precision=2).set_table_styles([
# # #         {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]}
# # #     ]))

# # # def render_group_analysis_section(processed_kharif, processed_water):
# # #     """Render the group analysis section of the dashboard"""
    
# # #     st.header("📋 Group Analysis & Data Export")
    
# # #     # Create groups
# # #     farm_groups = create_farm_groups(processed_kharif)
    
# # #     # Create merged datasets
# # #     merged_datasets = {}
    
# # #     # Overall dataset
# # #     overall_merged = merge_data_for_group(processed_kharif, processed_water, 'All Farms')
# # #     merged_datasets['All Farms'] = overall_merged
    
# # #     # Group-specific datasets
# # #     for group_name, group_df in farm_groups.items():
# # #         if group_name != 'All Farms':  # Skip overall as we already created it
# # #             group_merged = merge_data_for_group(group_df, processed_water, group_name)
# # #             merged_datasets[group_name] = group_merged
    
# # #     # Display results
# # #     st.subheader("Analysis Results")
    
# # #     selected_group = st.selectbox("Select Group to View", list(merged_datasets.keys()))
    
# # #     if selected_group in merged_datasets:
# # #         group_data = merged_datasets[selected_group]
        
# # #         st.write(f"**{selected_group}** - {len(group_data)} records")
        
# # #         if not group_data.empty:
# # #             st.dataframe(group_data.head(50))
            
# # #             # Summary statistics
# # #             st.subheader("Summary Statistics")
# # #             if 'Measure water level inside the PVC pipe - millimeter mm' in group_data.columns:
# # #                 water_levels = pd.to_numeric(group_data['Measure water level inside the PVC pipe - millimeter mm'], errors='coerce')
# # #                 water_levels = water_levels.dropna()
                
# # #                 if not water_levels.empty:
# # #                     col1, col2, col3, col4 = st.columns(4)
# # #                     with col1:
# # #                         st.metric("Mean Water Level (mm)", f"{water_levels.mean():.2f}")
# # #                     with col2:
# # #                         st.metric("Median Water Level (mm)", f"{water_levels.median():.2f}")
# # #                     with col3:
# # #                         st.metric("Min Water Level (mm)", f"{water_levels.min():.2f}")
# # #                     with col4:
# # #                         st.metric("Max Water Level (mm)", f"{water_levels.max():.2f}")
            
# # #             # Download option
# # #             csv_buffer = io.StringIO()
# # #             group_data.to_csv(csv_buffer, index=False)
# # #             csv_data = csv_buffer.getvalue()
            
# # #             st.download_button(
# # #                 label=f"Download {selected_group} Data as CSV",
# # #                 data=csv_data,
# # #                 file_name=f"farm_data_{selected_group.lower().replace(' ', '_')}.csv",
# # #                 mime="text/csv"
# # #             )
# # #         else:
# # #             st.warning(f"No data found for {selected_group}")
    
# # #     # Download all datasets
# # #     st.subheader("Download All Datasets")
    
# # #     if st.button("Generate All CSV Files"):
# # #         # Create a simple method to combine all CSVs into one download
# # #         all_data = []
# # #         for group_name, group_data in merged_datasets.items():
# # #             if not group_data.empty:
# # #                 all_data.append(group_data)
        
# # #         if all_data:
# # #             combined_data = pd.concat(all_data, ignore_index=True)
# # #             csv_buffer = io.StringIO()
# # #             combined_data.to_csv(csv_buffer, index=False)
# # #             csv_data = csv_buffer.getvalue()
            
# # #             st.download_button(
# # #                 label="Download Combined Data as CSV",
# # #                 data=csv_data,
# # #                 file_name="all_farm_data_combined.csv",
# # #                 mime="text/csv"
# # #             )
    
# # #     # Display group summary
# # #     st.subheader("Group Summary")
# # #     summary_data = []
# # #     for group_name, group_data in merged_datasets.items():
# # #         if not group_data.empty:
# # #             unique_farms = group_data['Kharif 25 Farm ID'].nunique()
# # #             total_records = len(group_data)
            
# # #             # Calculate water level stats if available
# # #             water_levels = pd.to_numeric(group_data['Measure water level inside the PVC pipe - millimeter mm'], errors='coerce')
# # #             water_levels = water_levels.dropna()
# # #             avg_water_level = water_levels.mean() if not water_levels.empty else 0
            
# # #             summary_data.append({
# # #                 'Group': group_name,
# # #                 'Unique Farms': unique_farms,
# # #                 'Total Records': total_records,
# # #                 'Avg Water Level (mm)': round(avg_water_level, 2) if avg_water_level > 0 else 'N/A'
# # #             })
    
# # #     if summary_data:
# # #         summary_df = pd.DataFrame(summary_data)
# # #         st.dataframe(summary_df)

# # # def merge_data_for_group(kharif_group, water_df, group_name):
# # #     """Merge Kharif and water data for a specific group"""
    
# # #     merged_data = []
    
# # #     for _, farm_row in kharif_group.iterrows():
# # #         farm_id = farm_row.get('Kharif 25 Farm ID', '')
# # #         tpr_date = farm_row.get('Kharif 25 Paddy transplanting date (TPR)', '2025-06-01')
        
# # #         # Get all pipe codes for this farm
# # #         pipe_codes = []
# # #         for i in range(1, 6):
# # #             pipe_col = f'Kharif 25 PVC Pipe code - {i}'
# # #             if pipe_col in farm_row.index and pd.notna(farm_row[pipe_col]):
# # #                 pipe_codes.append(farm_row[pipe_col])
        
# # #         # Match with water level data
# # #         farm_water_data = water_df[water_df['Farm ID'] == farm_id]
        
# # #         for _, water_row in farm_water_data.iterrows():
# # #             pipe_code = water_row.get('Pipe code ID of the farm', '')
            
# # #             # Check if this pipe code belongs to this farm
# # #             if pipe_code in pipe_codes or not pipe_codes:  # Include if pipe code matches or no pipe codes available
# # #                 merged_row = {
# # #                     'Group': group_name,
# # #                     'Kharif 25 Farm ID': farm_id,
# # #                     'Date': water_row.get('Date', ''),
# # #                     'Pipe code ID of the farm': pipe_code,
# # #                     'Measure water level inside the PVC pipe - millimeter mm': water_row.get('Measure water level inside the PVC pipe - millimeter mm', ''),
# # #                     'Kharif 25 Paddy transplanting date (TPR)': tpr_date
# # #                 }
# # #                 merged_data.append(merged_row)
    
# # #     return pd.DataFrame(merged_data)

# # # def main():
# # #     st.set_page_config(
# # #         page_title="Agricultural Data Analysis Dashboard",
# # #         page_icon="🌾",
# # #         layout="wide"
# # #     )
    
# # #     st.title("🌾 Agricultural Data Analysis Dashboard")
    
# # #     # Add button for 2024 data analysis
# # #     st.link_button("Analyze 2024 Data", "https://v45bgthcmmrztmbstkddra.streamlit.app/")
    
# # #     # Load data
# # #     kharif_df, water_df = load_data()

# # #     if kharif_df is not None and water_df is not None:
# # #         st.success("✅ Files loaded successfully!")
        
# # #         # Show data info in sidebar
# # #         with st.sidebar:
# # #             st.subheader("📊 Data Overview")
# # #             st.write(f"**Kharif Data:**")
# # #             st.write(f"• Rows: {len(kharif_df):,}")
# # #             st.write(f"• Columns: {len(kharif_df.columns)}")
# # #             st.write(f"**Water Level Data:**")
# # #             st.write(f"• Rows: {len(water_df):,}")
# # #             st.write(f"• Columns: {len(water_df.columns)}")
        
# # #         # Process data
# # #         with st.spinner("Processing data..."):
# # #             processed_kharif = process_kharif_data(kharif_df)
# # #             processed_water = process_water_data(water_df)
            
# # #             # Preprocess for visualization
# # #             merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg = preprocess_for_visualization(kharif_df, water_df)
            
# # #             # Create groups for visualization
# # #             groups = create_farm_groups(processed_kharif)
        
# # #         # Create tabs for different sections
# # #         tab1, tab2, tab3 = st.tabs(["🏡 Individual Farms", "👥 Group Analysis", "📋 Data Export"])
        
# # #         with tab1:
# # #             render_individual_farm_visualization(kharif_df, water_df, merged_df, farm_daily_avg, pipe_weekly_avg, farm_weekly_avg)
        
# # #         with tab2:
# # #             render_group_visualization(groups, farm_daily_avg, farm_weekly_avg)
        
# # #         with tab3:
# # #             render_group_analysis_section(processed_kharif, processed_water)
    
# # #     else:
# # #         st.info("📁 Please upload both Kharif Excel and Water Level Measurement Excel files to proceed.")
        
# # #         # Show example data structure
# # #         with st.expander("ℹ️ Expected Data Structure"):
# # #             st.markdown("""
# # #             **Kharif 25 Excel File should contain:**
# # #             - Kharif 25 Farm ID
# # #             - Kharif 25 Village
# # #             - Kharif 25 Paddy transplanting date (TPR)
# # #             - Various study group columns (TPR, DSR, Remote Controllers, AWD)
# # #             - PVC Pipe codes (1-5)
            
# # #             **Water Level Measurement Excel File should contain:**
# # #             - Date
# # #             - Farm ID
# # #             - Pipe code ID of the farm
# # #             - Measure water level inside the PVC pipe - millimeter mm
# # #             """)

# # # if __name__ == "__main__":
# # #     main()






# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # from datetime import datetime, timedelta
# # import plotly.graph_objects as go
# # import plotly.express as px
# # import io
# # import re
# # import zipfile
# # import warnings
# # warnings.filterwarnings('ignore')

# # # Configure page
# # st.set_page_config(
# #     page_title="Enhanced Agricultural Data Analysis Dashboard",
# #     page_icon="🌾",
# #     layout="wide"
# # )

# # # Custom CSS for better styling
# # st.markdown("""
# # <style>
# #     .main-header {
# #         font-size: 2.5rem;
# #         color: #2E7D32;
# #         text-align: center;
# #         margin-bottom: 2rem;
# #     }
# #     .section-header {
# #         font-size: 1.5rem;
# #         color: #1976D2;
# #         border-bottom: 2px solid #1976D2;
# #         padding-bottom: 0.5rem;
# #         margin: 1.5rem 0 1rem 0;
# #     }
# #     .metric-container {
# #         background-color: #f0f2f6;
# #         padding: 1rem;
# #         border-radius: 0.5rem;
# #         margin: 0.5rem 0;
# #     }
# #     .filter-section {
# #         background-color: #e8f5e8;
# #         padding: 1rem;
# #         border-radius: 0.5rem;
# #         margin-bottom: 1rem;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # def normalize_text(text):
# #     """Normalize text for consistent comparison"""
# #     if pd.isna(text) or text is None:
# #         return ""
# #     text = str(text).strip().lower()
# #     text = re.sub(r'\s+', ' ', text)
# #     text = re.sub(r'[^\w\s]', '', text)
# #     return text

# # def fuzzy_match_villages(village_list, threshold=85):
# #     """Group similar village names using simple similarity"""
# #     if not village_list:
# #         return []
    
# #     normalized_villages = {}
# #     for village in village_list:
# #         if pd.isna(village):
# #             continue
        
# #         norm_village = normalize_text(village)
# #         if not norm_village:
# #             continue
            
# #         # Check for exact matches first
# #         found_match = False
# #         for existing_norm, original in normalized_villages.items():
# #             if norm_village == existing_norm:
# #                 found_match = True
# #                 break
# #             # Simple similarity check
# #             if len(norm_village) > 3 and len(existing_norm) > 3:
# #                 if norm_village in existing_norm or existing_norm in norm_village:
# #                     found_match = True
# #                     break
        
# #         if not found_match:
# #             normalized_villages[norm_village] = str(village).strip()
    
# #     return sorted(list(normalized_villages.values()))

# # def load_and_validate_data():
# #     """Load and validate uploaded Excel files"""
# #     st.markdown('<div class="section-header">📁 Data Upload Section</div>', unsafe_allow_html=True)
    
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         st.markdown("**Upload Kharif 25 Excel File**")
# #         kharif_file = st.file_uploader(
# #             "Choose Kharif file", 
# #             type=['xlsx', 'xls'],
# #             help="Upload the main farm data file with study group information"
# #         )
# #         if kharif_file:
# #             st.success("✅ Kharif file uploaded successfully")
    
# #     with col2:
# #         st.markdown("**Upload Water Level Excel File**")
# #         water_file = st.file_uploader(
# #             "Choose Water Level file", 
# #             type=['xlsx', 'xls'],
# #             help="Upload the water level measurement data file"
# #         )
# #         if water_file:
# #             st.success("✅ Water level file uploaded successfully")
    
# #     if kharif_file is not None and water_file is not None:
# #         try:
# #             with st.spinner("📊 Loading and validating data..."):
# #                 # Load data
# #                 kharif_df = pd.read_excel(kharif_file)
# #                 water_df = pd.read_excel(water_file)
                
# #                 # Validate required columns
# #                 required_kharif_cols = [
# #                     'Kharif 25 Farm ID',
# #                     'Kharif 25 Village',
# #                     'Kharif 25 Paddy transplanting date (TPR)'
# #                 ]
                
# #                 required_water_cols = [
# #                     'Date',
# #                     'Farm ID',
# #                     'Pipe code ID of the farm',
# #                     'Measure water level inside the PVC pipe - millimeter mm'
# #                 ]
                
# #                 missing_kharif = [col for col in required_kharif_cols if col not in kharif_df.columns]
# #                 missing_water = [col for col in required_water_cols if col not in water_df.columns]
                
# #                 if missing_kharif:
# #                     st.error(f"❌ Missing columns in Kharif file: {missing_kharif}")
# #                     return None, None
                
# #                 if missing_water:
# #                     st.error(f"❌ Missing columns in Water file: {missing_water}")
# #                     return None, None
                
# #                 st.success("✅ Data validation completed successfully!")
# #                 return kharif_df, water_df
                
# #         except Exception as e:
# #             st.error(f"❌ Error loading files: {str(e)}")
# #             return None, None
    
# #     return None, None

# # def clean_and_process_data(kharif_df, water_df):
# #     """Enhanced data cleaning and processing"""
    
# #     kharif_cleaned = kharif_df.copy()
# #     water_cleaned = water_df.copy()
    
# #     # Clean and normalize text columns
# #     if 'Kharif 25 Village' in kharif_cleaned.columns:
# #         kharif_cleaned['Village_Normalized'] = kharif_cleaned['Kharif 25 Village'].apply(lambda x: normalize_text(x) if pd.notna(x) else "")
# #         kharif_cleaned['Kharif 25 Village'] = kharif_cleaned['Kharif 25 Village'].astype(str).str.strip()
    
# #     if 'Village name' in water_cleaned.columns:
# #         water_cleaned['Village_Normalized'] = water_cleaned['Village name'].apply(lambda x: normalize_text(x) if pd.notna(x) else "")
# #         water_cleaned['Village name'] = water_cleaned['Village name'].astype(str).str.strip()
    
# #     # Clean Farm IDs
# #     if 'Farm ID' in water_cleaned.columns:
# #         water_cleaned['Farm ID'] = water_cleaned['Farm ID'].astype(str).str.strip().str.upper()
    
# #     if 'Kharif 25 Farm ID' in kharif_cleaned.columns:
# #         kharif_cleaned['Kharif 25 Farm ID'] = kharif_cleaned['Kharif 25 Farm ID'].astype(str).str.strip().str.upper()
    
# #     # Handle dates properly
# #     if 'Date' in water_cleaned.columns:
# #         water_cleaned['Date'] = pd.to_datetime(water_cleaned['Date'], errors='coerce')
# #         water_cleaned = water_cleaned.dropna(subset=['Date'])
    
# #     if 'Kharif 25 Paddy transplanting date (TPR)' in kharif_cleaned.columns:
# #         kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'] = pd.to_datetime(
# #             kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'], errors='coerce'
# #         )
# #         # Fill missing TPR dates with June 1, 2025
# #         kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'].fillna(
# #             pd.Timestamp('2025-06-01'), inplace=True
# #         )
    
# #     # Clean water level measurements
# #     if 'Measure water level inside the PVC pipe - millimeter mm' in water_cleaned.columns:
# #         water_cleaned['Water_Level_Numeric'] = pd.to_numeric(
# #             water_cleaned['Measure water level inside the PVC pipe - millimeter mm'], 
# #             errors='coerce'
# #         )
# #         water_cleaned = water_cleaned.dropna(subset=['Water_Level_Numeric'])
    
# #     # Handle binary columns (Y/N to 1/0)
# #     binary_columns = [col for col in kharif_cleaned.columns if '(Y/N)' in col]
# #     for col in binary_columns:
# #         kharif_cleaned[col] = kharif_cleaned[col].fillna(0)
# #         kharif_cleaned[col] = kharif_cleaned[col].apply(lambda x: 1 if str(x).upper() in ['Y', 'YES', '1', 1] else 0)
    
# #     return kharif_cleaned, water_cleaned

# # def create_advanced_filters(kharif_df, water_df):
# #     """Create comprehensive filtering system"""
    
# #     st.sidebar.markdown('<div class="section-header">🔍 Advanced Filters</div>', unsafe_allow_html=True)
    
# #     filters = {}
    
# #     # Date Range Filter
# #     with st.sidebar.expander("📅 Date Range Filter", expanded=True):
# #         if 'Date' in water_df.columns and not water_df['Date'].isna().all():
# #             min_date = water_df['Date'].min().date()
# #             max_date = water_df['Date'].max().date()
            
# #             date_range = st.date_input(
# #                 "Select date range:",
# #                 value=(min_date, max_date),
# #                 min_value=min_date,
# #                 max_value=max_date
# #             )
            
# #             if len(date_range) == 2:
# #                 filters['date_range'] = date_range
# #                 st.info(f"📊 Selected: {date_range[0]} to {date_range[1]}")
    
# #     # Village Filter
# #     with st.sidebar.expander("🏘️ Village Filter", expanded=True):
# #         villages = []
# #         if 'Kharif 25 Village' in kharif_df.columns:
# #             villages.extend(kharif_df['Kharif 25 Village'].dropna().unique())
# #         if 'Village name' in water_df.columns:
# #             villages.extend(water_df['Village name'].dropna().unique())
        
# #         unique_villages = fuzzy_match_villages(list(set(villages)))
        
# #         selected_villages = st.multiselect(
# #             "Select villages:",
# #             options=unique_villages,
# #             default=[],
# #             help="Select specific villages to analyze"
# #         )
# #         filters['villages'] = selected_villages
        
# #         if selected_villages:
# #             st.info(f"📍 Selected {len(selected_villages)} village(s)")
    
# #     # Study Group Filters
# #     with st.sidebar.expander("🔬 Study Group Filters", expanded=True):
        
# #         # Remote Controllers Study
# #         st.markdown("**Remote Controllers Study:**")
# #         rc_filter = st.selectbox(
# #             "RC Group:",
# #             options=["All", "Treatment Group (A)", "Control Group (B)", "Complied Only", "Non-Complied Only"],
# #             help="Filter by Remote Controllers study groups"
# #         )
# #         filters['remote_controllers'] = rc_filter
        
# #         # AWD Study
# #         st.markdown("**AWD Study:**")
# #         awd_filter = st.selectbox(
# #             "AWD Group:",
# #             options=["All", "Group A (Treatment)", "Group B (Training)", "Group C (Control)", "Complied Only"],
# #             help="Filter by AWD study groups"
# #         )
# #         filters['awd_study'] = awd_filter
        
# #         # Farming Method
# #         st.markdown("**Farming Method:**")
# #         farming_method = st.selectbox(
# #             "Method:",
# #             options=["All", "TPR Only", "DSR Only"],
# #             help="Filter by farming method"
# #         )
# #         filters['farming_method'] = farming_method
    
# #     # Data Quality Filters
# #     with st.sidebar.expander("🔧 Data Quality", expanded=False):
        
# #         min_readings = st.number_input(
# #             "Min readings per farm:",
# #             min_value=1,
# #             max_value=100,
# #             value=1,
# #             help="Minimum number of water level readings per farm"
# #         )
# #         filters['min_readings'] = min_readings
        
# #         outlier_filter = st.checkbox(
# #             "Remove outliers",
# #             value=False,
# #             help="Remove statistical outliers from water level data"
# #         )
# #         filters['remove_outliers'] = outlier_filter
    
# #     return filters

# # def apply_comprehensive_filters(kharif_df, water_df, filters):
# #     """Apply all selected filters to the datasets"""
    
# #     filtered_kharif = kharif_df.copy()
# #     filtered_water = water_df.copy()
    
# #     # Apply date filter
# #     if 'date_range' in filters and len(filters['date_range']) == 2:
# #         start_date, end_date = filters['date_range']
# #         filtered_water = filtered_water[
# #             (filtered_water['Date'] >= pd.Timestamp(start_date)) &
# #             (filtered_water['Date'] <= pd.Timestamp(end_date))
# #         ]
    
# #     # Apply village filter
# #     if filters['villages']:
# #         # Normalize selected villages for comparison
# #         normalized_selected = [normalize_text(v) for v in filters['villages']]
        
# #         if 'Village_Normalized' in filtered_kharif.columns:
# #             filtered_kharif = filtered_kharif[
# #                 filtered_kharif['Village_Normalized'].isin(normalized_selected)
# #             ]
        
# #         if 'Village_Normalized' in filtered_water.columns:
# #             filtered_water = filtered_water[
# #                 filtered_water['Village_Normalized'].isin(normalized_selected)
# #             ]
    
# #     # Apply Remote Controllers filter
# #     if filters['remote_controllers'] != "All":
# #         if filters['remote_controllers'] == "Treatment Group (A)":
# #             mask = filtered_kharif.get('Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)', 0) == 1
# #         elif filters['remote_controllers'] == "Control Group (B)":
# #             mask = filtered_kharif.get('Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)', 0) == 1
# #         elif filters['remote_controllers'] == "Complied Only":
# #             mask_a = filtered_kharif.get('Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)', 0) == 1
# #             mask_b = filtered_kharif.get('Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)', 0) == 1
# #             mask = mask_a | mask_b
# #         elif filters['remote_controllers'] == "Non-Complied Only":
# #             mask_a = filtered_kharif.get('Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)', 0) == 1
# #             mask_b = filtered_kharif.get('Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)', 0) == 1
# #             mask = mask_a | mask_b
# #         else:
# #             mask = pd.Series([True] * len(filtered_kharif))
        
# #         filtered_kharif = filtered_kharif[mask]
    
# #     # Apply AWD filter
# #     if filters['awd_study'] != "All":
# #         if filters['awd_study'] == "Group A (Treatment)":
# #             mask = filtered_kharif.get('Kharif 25 - AWD Study - Group A - Treatment (Y/N)', 0) == 1
# #         elif filters['awd_study'] == "Group B (Training)":
# #             mask = filtered_kharif.get('Kharif 25 - AWD Study - Group B -training only (Y/N)', 0) == 1
# #         elif filters['awd_study'] == "Group C (Control)":
# #             mask = filtered_kharif.get('Kharif 25 - AWD Study - Group C - Control (Y/N)', 0) == 1
# #         elif filters['awd_study'] == "Complied Only":
# #             mask_a = filtered_kharif.get('Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)', 0) == 1
# #             mask_b = filtered_kharif.get('Kharif 25 - AWD Study - Group B - Complied (Y/N)', 0) == 1
# #             mask_c = filtered_kharif.get('Kharif 25 - AWD Study - Group C - Complied (Y/N)', 0) == 1
# #             mask = mask_a | mask_b | mask_c
# #         else:
# #             mask = pd.Series([True] * len(filtered_kharif))
        
# #         filtered_kharif = filtered_kharif[mask]
    
# #     # Apply farming method filter
# #     if filters['farming_method'] != "All":
# #         if filters['farming_method'] == "TPR Only":
# #             mask = filtered_kharif.get('Kharif 25 - TPR Group Study (Y/N)', 0) == 1
# #         elif filters['farming_method'] == "DSR Only":
# #             mask = filtered_kharif.get('Kharif 25 - DSR farm Study (Y/N)', 0) == 1
# #         else:
# #             mask = pd.Series([True] * len(filtered_kharif))
        
# #         filtered_kharif = filtered_kharif[mask]
    
# #     # Apply minimum readings filter
# #     if 'min_readings' in filters and filters['min_readings'] > 1:
# #         farm_counts = filtered_water['Farm ID'].value_counts()
# #         valid_farms = farm_counts[farm_counts >= filters['min_readings']].index
# #         filtered_water = filtered_water[filtered_water['Farm ID'].isin(valid_farms)]
    
# #     # Apply outlier removal
# #     if filters.get('remove_outliers', False) and 'Water_Level_Numeric' in filtered_water.columns:
# #         Q1 = filtered_water['Water_Level_Numeric'].quantile(0.25)
# #         Q3 = filtered_water['Water_Level_Numeric'].quantile(0.75)
# #         IQR = Q3 - Q1
# #         lower_bound = Q1 - 1.5 * IQR
# #         upper_bound = Q3 + 1.5 * IQR
        
# #         filtered_water = filtered_water[
# #             (filtered_water['Water_Level_Numeric'] >= lower_bound) &
# #             (filtered_water['Water_Level_Numeric'] <= upper_bound)
# #         ]
    
# #     return filtered_kharif, filtered_water

# # def create_merged_dataset(kharif_df, water_df):
# #     """Create comprehensive merged dataset with all calculations"""
    
# #     # Select relevant columns for merging
# #     kharif_cols = [
# #         "Kharif 25 Farm ID",
# #         "Kharif 25 Village",
# #         "Kharif 25 Paddy transplanting date (TPR)"
# #     ]
    
# #     # Add pipe code columns if they exist
# #     for i in range(1, 6):
# #         pipe_col = f"Kharif 25 PVC Pipe code - {i}"
# #         if pipe_col in kharif_df.columns:
# #             kharif_cols.append(pipe_col)
    
# #     kharif_subset = kharif_df[kharif_cols].copy()
    
# #     # Select water level columns
# #     water_cols = [
# #         "Date",
# #         "Farm ID",
# #         "Village name",
# #         "Pipe code ID of the farm"
# #     ]
    
# #     # Handle different possible column names for water level
# #     water_level_col = None
# #     possible_water_cols = [
# #         "Measure water level inside the PVC pipe - millimeter mm",
# #         "Water_Level_Numeric",
# #         "Water Level (mm)"
# #     ]
    
# #     for col in possible_water_cols:
# #         if col in water_df.columns:
# #             water_level_col = col
# #             break
    
# #     if water_level_col:
# #         water_cols.append(water_level_col)
    
# #     water_subset = water_df[water_cols].copy()
    
# #     # Merge datasets
# #     merged_df = pd.merge(
# #         water_subset,
# #         kharif_subset,
# #         how="inner",
# #         left_on="Farm ID",
# #         right_on="Kharif 25 Farm ID"
# #     )
    
# #     # Rename columns for clarity
# #     column_renames = {
# #         water_level_col: "Water Level (mm)",
# #         "Kharif 25 Paddy transplanting date (TPR)": "TPR Date",
# #         "Kharif 25 Village": "Village"
# #     }
    
# #     merged_df.rename(columns=column_renames, inplace=True)
    
# #     # Calculate days and weeks from TPR
# #     if 'TPR Date' in merged_df.columns and 'Date' in merged_df.columns:
# #         merged_df["Days from TPR"] = (merged_df["Date"] - merged_df["TPR Date"]).dt.days
# #         merged_df["Week from TPR"] = (merged_df["Days from TPR"] / 7).astype(int)
    
# #     # Calculate farm-level daily averages
# #     if 'Water Level (mm)' in merged_df.columns:
# #         farm_daily_avg = merged_df.groupby(['Farm ID', 'Date']).agg({
# #             'Water Level (mm)': 'mean',
# #             'TPR Date': 'first',
# #             'Village': 'first'
# #         }).reset_index()
        
# #         farm_daily_avg["Days from TPR"] = (farm_daily_avg["Date"] - farm_daily_avg["TPR Date"]).dt.days
# #         farm_daily_avg["Week from TPR"] = (farm_daily_avg["Days from TPR"] / 7).astype(int)
        
# #         # Calculate weekly averages
# #         weekly_avg = merged_df.groupby(['Farm ID', 'Week from TPR']).agg({
# #             'Water Level (mm)': 'mean',
# #             'Village': 'first'
# #         }).reset_index()
        
# #         return merged_df, farm_daily_avg, weekly_avg
    
# #     return merged_df, pd.DataFrame(), pd.DataFrame()

# # def render_individual_farm_analysis(merged_df, farm_daily_avg, weekly_avg):
# #     """Complete individual farm analysis with all required graphs and tables"""
    
# #     st.markdown('<div class="section-header">🏡 Individual Farm Analysis</div>', unsafe_allow_html=True)
    
# #     if merged_df.empty:
# #         st.warning("⚠️ No data available for individual farm analysis. Please check your filters.")
# #         return
    
# #     # Farm selection with search
# #     farm_ids = sorted(merged_df["Farm ID"].dropna().unique())
    
# #     col1, col2 = st.columns([2, 1])
    
# #     with col1:
# #         selected_farm = st.selectbox(
# #             "🔍 Select Farm ID:",
# #             options=farm_ids,
# #             help="Choose a farm to analyze in detail"
# #         )
    
# #     with col2:
# #         if selected_farm:
# #             farm_info = merged_df[merged_df["Farm ID"] == selected_farm].iloc[0]
# #             village = farm_info.get('Village', 'Unknown')
# #             st.info(f"📍 Village: {village}")
    
# #     if not selected_farm:
# #         st.warning("Please select a farm ID to proceed.")
# #         return
    
# #     # Filter data for selected farm
# #     farm_data = merged_df[merged_df["Farm ID"] == selected_farm].copy()
# #     farm_daily_data = farm_daily_avg[farm_daily_avg["Farm ID"] == selected_farm].copy()
# #     farm_weekly_data = weekly_avg[weekly_avg["Farm ID"] == selected_farm].copy()
    
# #     if farm_data.empty:
# #         st.warning(f"⚠️ No data found for Farm ID: {selected_farm}")
# #         return
    
# #     # Get available pipes
# #     available_pipes = sorted(farm_data["Pipe code ID of the farm"].dropna().unique())
    
# #     col1, col2 = st.columns([3, 1])
    
# #     with col1:
# #         selected_pipes = st.multiselect(
# #             "🔧 Select Pipes to Analyze:",
# #             options=available_pipes,
# #             default=available_pipes[:3] if len(available_pipes) > 3 else available_pipes,
# #             help="Choose which pipes to include in the analysis"
# #         )
    
# #     with col2:
# #         st.metric("📊 Total Readings", len(farm_data))
# #         st.metric("🔧 Available Pipes", len(available_pipes))
    
# #     if not selected_pipes:
# #         st.warning("⚠️ Please select at least one pipe to analyze.")
# #         return
    
# #     # Filter for selected pipes
# #     filtered_farm_data = farm_data[farm_data["Pipe code ID of the farm"].isin(selected_pipes)].copy()
    
# #     # **GRAPH 1: Daily Water Levels per Pipe + Farm Average**
# #     st.markdown("### 📊 Graph 1: Daily Water Levels per Pipe + Farm Average")
    
# #     fig1 = go.Figure()
    
# #     # Color palette for pipes
# #     colors = px.colors.qualitative.Set3
    
# #     # Add each pipe as markers only
# #     for i, pipe in enumerate(selected_pipes):
# #         pipe_data = filtered_farm_data[filtered_farm_data["Pipe code ID of the farm"] == pipe].copy()
# #         pipe_data = pipe_data.sort_values("Days from TPR")
        
# #         fig1.add_trace(go.Scatter(
# #             x=pipe_data["Days from TPR"],
# #             y=pipe_data["Water Level (mm)"],
# #             mode='markers',
# #             name=f"Pipe {pipe}",
# #             marker=dict(
# #                 size=8,
# #                 color=colors[i % len(colors)],
# #                 opacity=0.7
# #             ),
# #             hovertemplate="<b>Pipe %{text}</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>",
# #             text=[pipe] * len(pipe_data)
# #         ))
    
# #     # Add farm average as line + markers
# #     if not farm_daily_data.empty:
# #         farm_daily_sorted = farm_daily_data.sort_values("Days from TPR")
# #         fig1.add_trace(go.Scatter(
# #             x=farm_daily_sorted["Days from TPR"],
# #             y=farm_daily_sorted["Water Level (mm)"],
# #             mode='lines+markers',
# #             name="Farm Average",
# #             line=dict(width=4, color='white'),
# #             marker=dict(symbol='diamond', size=12, color='white'),
# #             hovertemplate="<b>Farm Average</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>"
# #         ))
    
# #     fig1.update_layout(
# #         title=f"Daily Water Levels - Farm {selected_farm}",
# #         xaxis_title="Days from Transplanting",
# #         yaxis_title="PVC Water Level (mm)",
# #         legend=dict(
# #             orientation="h",
# #             yanchor="bottom",
# #             y=1.02,
# #             xanchor="right",
# #             x=1
# #         ),
# #         hovermode="x unified",
# #         height=500,
# #         showlegend=True
# #     )
    
# #     st.plotly_chart(fig1, use_container_width=True)
    
# #     # **GRAPH 2: Weekly Water Level Trends**
# #     st.markdown("### 📈 Graph 2: Weekly Water Level Trends per Pipe + Farm Average")
    
# #     fig2 = go.Figure()
    
# #     # Weekly averages per pipe (markers only)
# #     for i, pipe in enumerate(selected_pipes):
# #         pipe_data = filtered_farm_data[filtered_farm_data["Pipe code ID of the farm"] == pipe]
# #         pipe_weekly = pipe_data.groupby("Week from TPR")["Water Level (mm)"].mean().reset_index()
# #         pipe_weekly = pipe_weekly.sort_values("Week from TPR")
        
# #         fig2.add_trace(go.Scatter(
# #             x=pipe_weekly["Week from TPR"],
# #             y=pipe_weekly["Water Level (mm)"],
# #             mode='markers',
# #             name=f"Pipe {pipe}",
# #             marker=dict(
# #                 size=10,
# #                 color=colors[i % len(colors)],
# #                 opacity=0.7
# #             ),
# #             hovertemplate="<b>Pipe %{text}</b><br>" +
# #                          "Week from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>",
# #             text=[pipe] * len(pipe_weekly)
# #         ))
    
# #     # Farm weekly average (line + markers)
# #     if not farm_weekly_data.empty:
# #         farm_weekly_sorted = farm_weekly_data.sort_values("Week from TPR")
# #         fig2.add_trace(go.Scatter(
# #             x=farm_weekly_sorted["Week from TPR"],
# #             y=farm_weekly_sorted["Water Level (mm)"],
# #             mode='lines+markers',
# #             name="Farm Weekly Average",
# #             line=dict(width=4, color='white'),
# #             marker=dict(symbol='diamond', size=12, color='white'),
# #             hovertemplate="<b>Farm Weekly Average</b><br>" +
# #                          "Week from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>"
# #         ))
    
# #     fig2.update_layout(
# #         title=f"Weekly Water Level Trends - Farm {selected_farm}",
# #         xaxis_title="Weeks from Transplanting",
# #         yaxis_title="PVC Water Level (mm)",
# #         legend=dict(
# #             orientation="h",
# #             yanchor="bottom",
# #             y=1.02,
# #             xanchor="right",
# #             x=1
# #         ),
# #         hovermode="x unified",
# #         height=500,
# #         showlegend=True
# #     )
    
# #     st.plotly_chart(fig2, use_container_width=True)
    
# #     # **TABLE 3: Water Level Data (All Pipes) - As Required**
# #     st.markdown("### 📋 Table 3: Water Level Data (All Pipes)")
# #     st.markdown("*Individual pipe readings with timestamps and farm averages*")
    
# #     # Create comprehensive table with Days from TPR as Column A
# #     table_data = filtered_farm_data.pivot_table(
# #         index="Days from TPR",
# #         columns="Pipe code ID of the farm",
# #         values="Water Level (mm)",
# #         aggfunc='mean'
# #     ).reset_index()
    
# #     # Add farm average column
# #     if not farm_daily_data.empty:
# #         farm_avg_for_table = farm_daily_data.set_index("Days from TPR")["Water Level (mm)"]
# #         table_data = table_data.set_index("Days from TPR")
# #         table_data["Farm Average"] = farm_avg_for_table
# #         table_data = table_data.reset_index()
    
# #     # Add date column for timestamps
# #     date_mapping = filtered_farm_data.groupby("Days from TPR")["Date"].first().reset_index()
# #     table_data = pd.merge(table_data, date_mapping, on="Days from TPR", how="left")
    
# #     # Reorder columns: Days from TPR (Column A), Date, Pipes, Farm Average
# #     pipe_cols = [col for col in table_data.columns if col not in ["Days from TPR", "Date", "Farm Average"]]
# #     column_order = ["Days from TPR", "Date"] + sorted(pipe_cols) + (["Farm Average"] if "Farm Average" in table_data.columns else [])
# #     table_data = table_data[column_order]
    
# #     # Format the table
# #     st.dataframe(
# #         table_data.style.format({
# #             col: "{:.1f}" for col in table_data.columns if col not in ["Days from TPR", "Date"]
# #         }).set_table_styles([
# #             {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]},
# #             {'selector': 'td', 'props': [('text-align', 'center')]}
# #         ]),
# #         use_container_width=True,
# #         height=400
# #     )
    
# #     # Summary statistics
# #     st.markdown("### 📊 Farm Summary Statistics")
    
# #     col1, col2, col3, col4 = st.columns(4)
    
# #     with col1:
# #         avg_level = filtered_farm_data["Water Level (mm)"].mean()
# #         st.metric("🌊 Average Water Level", f"{avg_level:.1f} mm")
    
# #     with col2:
# #         std_level = filtered_farm_data["Water Level (mm)"].std()
# #         st.metric("📏 Standard Deviation", f"{std_level:.1f} mm")
    
# #     with col3:
# #         min_level = filtered_farm_data["Water Level (mm)"].min()
# #         st.metric("⬇️ Minimum Level", f"{min_level:.1f} mm")
    
# #     with col4:
# #         max_level = filtered_farm_data["Water Level (mm)"].max()
# #         st.metric("⬆️ Maximum Level", f"{max_level:.1f} mm")
    
# #     # Download section for individual farm
# #     st.markdown("### 💾 Download Individual Farm Data")
    
# #     col1, col2, col3 = st.columns(3)
    
# #     with col1:
# #         # Download detailed data
# #         csv_buffer = io.StringIO()
# #         filtered_farm_data.to_csv(csv_buffer, index=False)
# #         st.download_button(
# #             label="📥 Download Detailed Data",
# #             data=csv_buffer.getvalue(),
# #             file_name=f"farm_{selected_farm}_detailed_data.csv",
# #             mime="text/csv",
# #             help="All individual readings for this farm"
# #         )
    
# #     with col2:
# #         # Download summary table
# #         csv_buffer = io.StringIO()
# #         table_data.to_csv(csv_buffer, index=False)
# #         st.download_button(
# #             label="📥 Download Summary Table",
# #             data=csv_buffer.getvalue(),
# #             file_name=f"farm_{selected_farm}_summary_table.csv",
# #             mime="text/csv",
# #             help="Table 3 data as shown above"
# #         )
    
# #     with col3:
# #         # Download daily averages
# #         if not farm_daily_data.empty:
# #             csv_buffer = io.StringIO()
# #             farm_daily_data.to_csv(csv_buffer, index=False)
# #             st.download_button(
# #                 label="📥 Download Daily Averages",
# #                 data=csv_buffer.getvalue(),
# #                 file_name=f"farm_{selected_farm}_daily_averages.csv",
# #                 mime="text/csv",
# #                 help="Farm daily average calculations"
# #             )

# # def render_comparative_analysis(merged_df, kharif_df):
# #     """Comprehensive comparative analysis with all study group comparisons"""
    
# #     st.markdown('<div class="section-header">👥 Comparative Analysis</div>', unsafe_allow_html=True)
    
# #     if merged_df.empty:
# #         st.warning("⚠️ No data available for comparative analysis. Please check your filters.")
# #         return
    
# #     # Analysis type selection
# #     analysis_type = st.selectbox(
# #         "📊 Select Analysis Type:",
# #         options=[
# #             "Village-level Aggregations",
# #             "Remote Controllers: Treatment vs Control (Complied Groups)",
# #             "AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)",
# #             "DSR vs TPR Group Comparisons",
# #             "Comprehensive Compliance Analysis"
# #         ],
# #         help="Choose the type of comparative analysis to perform"
# #     )
    
# #     if analysis_type == "Village-level Aggregations":
# #         render_village_level_analysis(merged_df)
# #     elif analysis_type == "Remote Controllers: Treatment vs Control (Complied Groups)":
# #         render_remote_controllers_analysis(merged_df, kharif_df)
# #     elif analysis_type == "AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)":
# #         render_awd_groups_analysis(merged_df, kharif_df)
# #     elif analysis_type == "DSR vs TPR Group Comparisons":
# #         render_dsr_tpr_analysis(merged_df, kharif_df)
# #     elif analysis_type == "Comprehensive Compliance Analysis":
# #         render_compliance_analysis(merged_df, kharif_df)

# # def render_village_level_analysis(merged_df):
# #     """Village-level aggregations showing all farms"""
    
# #     st.markdown("### 🏘️ Village-level Water Level Aggregations")
# #     st.markdown("*Showing all farms aggregated by village*")
    
# #     if 'Village' not in merged_df.columns:
# #         st.error("Village information not available in the data.")
# #         return
    
# #     # Calculate village-level daily averages
# #     village_daily = merged_df.groupby(['Village', 'Days from TPR']).agg({
# #         'Water Level (mm)': 'mean',
# #         'Farm ID': 'nunique'
# #     }).reset_index()
    
# #     village_daily.rename(columns={'Farm ID': 'Farm Count'}, inplace=True)
    
# #     # Create village comparison chart
# #     fig = go.Figure()
    
# #     villages = sorted(village_daily['Village'].unique())
# #     colors = px.colors.qualitative.Set3
    
# #     for i, village in enumerate(villages):
# #         village_data = village_daily[village_daily['Village'] == village]
# #         village_data = village_data.sort_values('Days from TPR')
        
# #         fig.add_trace(go.Scatter(
# #             x=village_data['Days from TPR'],
# #             y=village_data['Water Level (mm)'],
# #             mode='lines+markers',
# #             name=village,
# #             line=dict(color=colors[i % len(colors)], width=3),
# #             marker=dict(size=8),
# #             hovertemplate="<b>%{text}</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>",
# #             text=[village] * len(village_data)
# #         ))
    
# #     fig.update_layout(
# #         title="Village-level Water Level Trends Comparison",
# #         xaxis_title="Days from Transplanting",
# #         yaxis_title="Average Water Level (mm)",
# #         legend=dict(
# #             orientation="v",
# #             yanchor="middle",
# #             y=0.5,
# #             xanchor="left",
# #             x=1.02
# #         ),
# #         height=600,
# #         hovermode="x unified"
# #     )
    
# #     st.plotly_chart(fig, use_container_width=True)
    
# #     # Village summary statistics table
# #     st.markdown("### 📊 Village Summary Statistics")
    
# #     village_summary = merged_df.groupby('Village').agg({
# #         'Water Level (mm)': ['mean', 'std', 'min', 'max', 'count'],
# #         'Farm ID': 'nunique',
# #         'Days from TPR': ['min', 'max']
# #     }).round(2)
    
# #     # Flatten column names
# #     village_summary.columns = [
# #         'Avg Water Level (mm)', 'Std Dev (mm)', 'Min Level (mm)', 
# #         'Max Level (mm)', 'Total Readings', 'Unique Farms',
# #         'Min Days from TPR', 'Max Days from TPR'
# #     ]
    
# #     village_summary = village_summary.reset_index()
    
# #     st.dataframe(
# #         village_summary.style.format({
# #             'Avg Water Level (mm)': '{:.1f}',
# #             'Std Dev (mm)': '{:.1f}',
# #             'Min Level (mm)': '{:.1f}',
# #             'Max Level (mm)': '{:.1f}'
# #         }),
# #         use_container_width=True
# #     )
    
# #     # Download village analysis
# #     csv_buffer = io.StringIO()
# #     village_summary.to_csv(csv_buffer, index=False)
# #     st.download_button(
# #         label="📥 Download Village Analysis",
# #         data=csv_buffer.getvalue(),
# #         file_name="village_level_analysis.csv",
# #         mime="text/csv"
# #     )

# # def render_remote_controllers_analysis(merged_df, kharif_df):
# #     """Remote Controllers: Treatment vs Control (Complied Groups)"""
    
# #     st.markdown("### 🎛️ Remote Controllers Study: Treatment vs Control")
# #     st.markdown("*Comparing complied groups from treatment and control*")
    
# #     # Create study group classifications
# #     study_data = pd.merge(
# #         merged_df,
# #         kharif_df[[
# #             'Kharif 25 Farm ID',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'
# #         ]],
# #         left_on='Farm ID',
# #         right_on='Kharif 25 Farm ID',
# #         how='left'
# #     )
    
# #     # Filter for complied groups
# #     treatment_complied = study_data[
# #         study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'] == 1
# #     ]
    
# #     control_complied = study_data[
# #         study_data['Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'] == 1
# #     ]
    
# #     if treatment_complied.empty and control_complied.empty:
# #         st.warning("⚠️ No Remote Controllers study data found with compliance information.")
# #         return
    
# #     # Create comparison chart
# #     fig = go.Figure()
    
# #     if not treatment_complied.empty:
# #         treatment_daily = treatment_complied.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #         treatment_daily = treatment_daily.sort_values('Days from TPR')
        
# #         fig.add_trace(go.Scatter(
# #             x=treatment_daily['Days from TPR'],
# #             y=treatment_daily['Water Level (mm)'],
# #             mode='lines+markers',
# #             name='Treatment Group (A) - Complied',
# #             line=dict(color='blue', width=4),
# #             marker=dict(size=10),
# #             hovertemplate="<b>Treatment Group (Complied)</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>"
# #         ))
    
# #     if not control_complied.empty:
# #         control_daily = control_complied.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #         control_daily = control_daily.sort_values('Days from TPR')
        
# #         fig.add_trace(go.Scatter(
# #             x=control_daily['Days from TPR'],
# #             y=control_daily['Water Level (mm)'],
# #             mode='lines+markers',
# #             name='Control Group (B) - Complied',
# #             line=dict(color='red', width=4),
# #             marker=dict(size=10),
# #             hovertemplate="<b>Control Group (Complied)</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>"
# #         ))
    
# #     fig.update_layout(
# #         title="Remote Controllers Study: Treatment vs Control (Complied Groups)",
# #         xaxis_title="Days from Transplanting",
# #         yaxis_title="Average Water Level (mm)",
# #         height=500,
# #         hovermode="x unified"
# #     )
    
# #     st.plotly_chart(fig, use_container_width=True)
    
# #     # Summary statistics
# #     st.markdown("### 📊 Group Comparison Statistics")
    
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         if not treatment_complied.empty:
# #             st.markdown("**Treatment Group (A) - Complied:**")
# #             st.metric("👥 Farms", treatment_complied['Farm ID'].nunique())
# #             st.metric("📊 Avg Water Level", f"{treatment_complied['Water Level (mm)'].mean():.1f} mm")
# #             st.metric("📏 Std Deviation", f"{treatment_complied['Water Level (mm)'].std():.1f} mm")
    
# #     with col2:
# #         if not control_complied.empty:
# #             st.markdown("**Control Group (B) - Complied:**")
# #             st.metric("👥 Farms", control_complied['Farm ID'].nunique())
# #             st.metric("📊 Avg Water Level", f"{control_complied['Water Level (mm)'].mean():.1f} mm")
# #             st.metric("📏 Std Deviation", f"{control_complied['Water Level (mm)'].std():.1f} mm")

# # def render_awd_groups_analysis(merged_df, kharif_df):
# #     """AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)"""
    
# #     st.markdown("### 💧 AWD Study: Groups A, B, C Comparisons")
# #     st.markdown("*Analyzing complied and non-complied groups across all AWD study groups*")
    
# #     # Create study group classifications
# #     study_data = pd.merge(
# #         merged_df,
# #         kharif_df[[
# #             'Kharif 25 Farm ID',
# #             'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group B -training only (Y/N)',
# #             'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - Control (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
# #         ]],
# #         left_on='Farm ID',
# #         right_on='Kharif 25 Farm ID',
# #         how='left'
# #     )
    
# #     # Create group filters
# #     groups_data = {}
    
# #     # Group A - Treatment
# #     groups_data['Group A (Treatment) - Complied'] = study_data[
# #         study_data['Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'] == 1
# #     ]
# #     groups_data['Group A (Treatment) - Non-Complied'] = study_data[
# #         study_data['Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)'] == 1
# #     ]
    
# #     # Group B - Training
# #     groups_data['Group B (Training) - Complied'] = study_data[
# #         study_data['Kharif 25 - AWD Study - Group B - Complied (Y/N)'] == 1
# #     ]
# #     groups_data['Group B (Training) - Non-Complied'] = study_data[
# #         study_data['Kharif 25 - AWD Study - Group B - Non-complied (Y/N)'] == 1
# #     ]
    
# #     # Group C - Control
# #     groups_data['Group C (Control) - Complied'] = study_data[
# #         study_data['Kharif 25 - AWD Study - Group C - Complied (Y/N)'] == 1
# #     ]
# #     groups_data['Group C (Control) - Non-Complied'] = study_data[
# #         study_data['Kharif 25 - AWD Study - Group C - non-complied (Y/N)'] == 1
# #     ]
    
# #     # Filter out empty groups
# #     available_groups = {k: v for k, v in groups_data.items() if not v.empty}
    
# #     if not available_groups:
# #         st.warning("⚠️ No AWD study data found.")
# #         return
    
# #     # Analysis options
# #     analysis_option = st.selectbox(
# #         "📊 Choose Analysis View:",
# #         options=[
# #             "All Groups Comparison",
# #             "Complied vs Non-Complied Comparison",
# #             "Group-wise Detailed Analysis"
# #         ]
# #     )
    
# #     if analysis_option == "All Groups Comparison":
# #         # Create comprehensive comparison chart
# #         fig = go.Figure()
# #         colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        
# #         for i, (group_name, group_data) in enumerate(available_groups.items()):
# #             if not group_data.empty:
# #                 daily_avg = group_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #                 daily_avg = daily_avg.sort_values('Days from TPR')
                
# #                 fig.add_trace(go.Scatter(
# #                     x=daily_avg['Days from TPR'],
# #                     y=daily_avg['Water Level (mm)'],
# #                     mode='lines+markers',
# #                     name=group_name,
# #                     line=dict(color=colors[i % len(colors)], width=3),
# #                     marker=dict(size=8)
# #                 ))
        
# #         fig.update_layout(
# #             title="AWD Study: All Groups Comparison",
# #             xaxis_title="Days from Transplanting",
# #             yaxis_title="Average Water Level (mm)",
# #             height=600,
# #             hovermode="x unified"
# #         )
        
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     elif analysis_option == "Complied vs Non-Complied Comparison":
# #         # Aggregate complied vs non-complied across all groups
# #         complied_data = pd.concat([
# #             groups_data['Group A (Treatment) - Complied'],
# #             groups_data['Group B (Training) - Complied'],
# #             groups_data['Group C (Control) - Complied']
# #         ]).drop_duplicates()
        
# #         non_complied_data = pd.concat([
# #             groups_data['Group A (Treatment) - Non-Complied'],
# #             groups_data['Group B (Training) - Non-Complied'],
# #             groups_data['Group C (Control) - Non-Complied']
# #         ]).drop_duplicates()
        
# #         fig = go.Figure()
        
# #         if not complied_data.empty:
# #             complied_daily = complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #             fig.add_trace(go.Scatter(
# #                 x=complied_daily['Days from TPR'],
# #                 y=complied_daily['Water Level (mm)'],
# #                 mode='lines+markers',
# #                 name='All Complied Groups',
# #                 line=dict(color='green', width=4),
# #                 marker=dict(size=10)
# #             ))
        
# #         if not non_complied_data.empty:
# #             non_complied_daily = non_complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #             fig.add_trace(go.Scatter(
# #                 x=non_complied_daily['Days from TPR'],
# #                 y=non_complied_daily['Water Level (mm)'],
# #                 mode='lines+markers',
# #                 name='All Non-Complied Groups',
# #                 line=dict(color='red', width=4),
# #                 marker=dict(size=10)
# #             ))
        
# #         fig.update_layout(
# #             title="AWD Study: Complied vs Non-Complied Comparison",
# #             xaxis_title="Days from Transplanting",
# #             yaxis_title="Average Water Level (mm)",
# #             height=500
# #         )
        
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     # Summary statistics table
# #     st.markdown("### 📊 AWD Groups Summary Statistics")
    
# #     summary_data = []
# #     for group_name, group_data in available_groups.items():
# #         if not group_data.empty:
# #             summary_data.append({
# #                 'Group': group_name,
# #                 'Farms': group_data['Farm ID'].nunique(),
# #                 'Total Readings': len(group_data),
# #                 'Avg Water Level (mm)': round(group_data['Water Level (mm)'].mean(), 1),
# #                 'Std Dev (mm)': round(group_data['Water Level (mm)'].std(), 1),
# #                 'Min Level (mm)': round(group_data['Water Level (mm)'].min(), 1),
# #                 'Max Level (mm)': round(group_data['Water Level (mm)'].max(), 1)
# #             })
    
# #     if summary_data:
# #         summary_df = pd.DataFrame(summary_data)
# #         st.dataframe(summary_df, use_container_width=True)

# # def render_dsr_tpr_analysis(merged_df, kharif_df):
# #     """DSR vs TPR Group Comparisons"""
    
# #     st.markdown("### 🌱 DSR vs TPR Farming Methods Comparison")
# #     st.markdown("*Comparing Direct Seeded Rice vs Transplanted Rice methods*")
    
# #     # Create study group classifications
# #     study_data = pd.merge(
# #         merged_df,
# #         kharif_df[[
# #             'Kharif 25 Farm ID',
# #             'Kharif 25 - DSR farm Study (Y/N)',
# #             'Kharif 25 - TPR Group Study (Y/N)'
# #         ]],
# #         left_on='Farm ID',
# #         right_on='Kharif 25 Farm ID',
# #         how='left'
# #     )
    
# #     # Filter for each method
# #     dsr_farms = study_data[study_data['Kharif 25 - DSR farm Study (Y/N)'] == 1]
# #     tpr_farms = study_data[study_data['Kharif 25 - TPR Group Study (Y/N)'] == 1]
    
# #     if dsr_farms.empty and tpr_farms.empty:
# #         st.warning("⚠️ No DSR or TPR study data found.")
# #         return
    
# #     # Create comparison chart
# #     fig = go.Figure()
    
# #     if not dsr_farms.empty:
# #         dsr_daily = dsr_farms.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #         dsr_daily = dsr_daily.sort_values('Days from TPR')
        
# #         fig.add_trace(go.Scatter(
# #             x=dsr_daily['Days from TPR'],
# #             y=dsr_daily['Water Level (mm)'],
# #             mode='lines+markers',
# #             name='DSR (Direct Seeded Rice)',
# #             line=dict(color='green', width=4),
# #             marker=dict(size=10, symbol='circle'),
# #             hovertemplate="<b>DSR Method</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>"
# #         ))
    
# #     if not tpr_farms.empty:
# #         tpr_daily = tpr_farms.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
# #         tpr_daily = tpr_daily.sort_values('Days from TPR')
        
# #         fig.add_trace(go.Scatter(
# #             x=tpr_daily['Days from TPR'],
# #             y=tpr_daily['Water Level (mm)'],
# #             mode='lines+markers',
# #             name='TPR (Transplanted Rice)',
# #             line=dict(color='blue', width=4),
# #             marker=dict(size=10, symbol='diamond'),
# #             hovertemplate="<b>TPR Method</b><br>" +
# #                          "Days from TPR: %{x}<br>" +
# #                          "Avg Water Level: %{y:.1f} mm<br>" +
# #                          "<extra></extra>"
# #         ))
    
# #     fig.update_layout(
# #         title="Farming Methods Comparison: DSR vs TPR",
# #         xaxis_title="Days from Transplanting/Seeding",
# #         yaxis_title="Average Water Level (mm)",
# #         height=500,
# #         hovermode="x unified"
# #     )
    
# #     st.plotly_chart(fig, use_container_width=True)
    
# #     # Comparative statistics
# #     st.markdown("### 📊 Method Comparison Statistics")
    
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         if not dsr_farms.empty:
# #             st.markdown("**DSR (Direct Seeded Rice):**")
# #             st.metric("👥 Farms", dsr_farms['Farm ID'].nunique())
# #             st.metric("📊 Avg Water Level", f"{dsr_farms['Water Level (mm)'].mean():.1f} mm")
# #             st.metric("📏 Std Deviation", f"{dsr_farms['Water Level (mm)'].std():.1f} mm")
# #             st.metric("📈 Total Readings", len(dsr_farms))
    
# #     with col2:
# #         if not tpr_farms.empty:
# #             st.markdown("**TPR (Transplanted Rice):**")
# #             st.metric("👥 Farms", tpr_farms['Farm ID'].nunique())
# #             st.metric("📊 Avg Water Level", f"{tpr_farms['Water Level (mm)'].mean():.1f} mm")
# #             st.metric("📏 Std Deviation", f"{tpr_farms['Water Level (mm)'].std():.1f} mm")
# #             st.metric("📈 Total Readings", len(tpr_farms))

# # def render_compliance_analysis(merged_df, kharif_df):
# #     """Comprehensive Compliance Analysis"""
    
# #     st.markdown("### ✅ Comprehensive Compliance Analysis")
# #     st.markdown("*Analyzing compliance rates across all studies*")
    
# #     # Create comprehensive study classifications
# #     study_data = pd.merge(
# #         merged_df,
# #         kharif_df[[
# #             'Kharif 25 Farm ID',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group B -training only (Y/N)',
# #             'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - Control (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
# #         ]],
# #         left_on='Farm ID',
# #         right_on='Kharif 25 Farm ID',
# #         how='left'
# #     )
    
# #     # Calculate compliance rates
# #     compliance_data = []
    
# #     # Remote Controllers compliance
# #     studies = [
# #         {
# #             'study': 'Remote Controllers - Treatment (A)',
# #             'total_col': 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
# #             'complied_col': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'
# #         },
# #         {
# #             'study': 'Remote Controllers - Control (B)',
# #             'total_col': 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
# #             'complied_col': 'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'
# #         },
# #         {
# #             'study': 'AWD - Group A (Treatment)',
# #             'total_col': 'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
# #             'complied_col': 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'
# #         },
# #         {
# #             'study': 'AWD - Group B (Training)',
# #             'total_col': 'Kharif 25 - AWD Study - Group B -training only (Y/N)',
# #             'complied_col': 'Kharif 25 - AWD Study - Group B - Complied (Y/N)'
# #         },
# #         {
# #             'study': 'AWD - Group C (Control)',
# #             'total_col': 'Kharif 25 - AWD Study - Group C - Control (Y/N)',
# #             'complied_col': 'Kharif 25 - AWD Study - Group C - Complied (Y/N)'
# #         }
# #     ]
    
# #     for study_info in studies:
# #         total_farms = len(study_data[study_data[study_info['total_col']] == 1]['Farm ID'].unique())
# #         complied_farms = len(study_data[study_data[study_info['complied_col']] == 1]['Farm ID'].unique())
        
# #         if total_farms > 0:
# #             compliance_rate = (complied_farms / total_farms) * 100
# #             compliance_data.append({
# #                 'Study Group': study_info['study'],
# #                 'Total Farms': total_farms,
# #                 'Complied Farms': complied_farms,
# #                 'Non-Complied Farms': total_farms - complied_farms,
# #                 'Compliance Rate (%)': round(compliance_rate, 1)
# #             })
    
# #     if not compliance_data:
# #         st.warning("⚠️ No compliance data found.")
# #         return
    
# #     # Display compliance table
# #     compliance_df = pd.DataFrame(compliance_data)
# #     st.dataframe(compliance_df, use_container_width=True)
    
# #     # Compliance visualization
# #     fig = go.Figure()
    
# #     fig.add_trace(go.Bar(
# #         x=compliance_df['Study Group'],
# #         y=compliance_df['Compliance Rate (%)'],
# #         text=compliance_df['Compliance Rate (%)'].apply(lambda x: f"{x:.1f}%"),
# #         textposition='auto',
# #         marker_color='lightblue',
# #         name='Compliance Rate'
# #     ))
    
# #     fig.update_layout(
# #         title="Compliance Rates Across All Studies",
# #         xaxis_title="Study Groups",
# #         yaxis_title="Compliance Rate (%)",
# #         height=400,
# #         xaxis_tickangle=-45
# #     )
    
# #     st.plotly_chart(fig, use_container_width=True)
    
# #     # Detailed compliance analysis
# #     st.markdown("### 📊 Detailed Compliance Breakdown")
    
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         # Overall compliance metrics
# #         total_participants = compliance_df['Total Farms'].sum()
# #         total_complied = compliance_df['Complied Farms'].sum()
# #         overall_compliance = (total_complied / total_participants) * 100 if total_participants > 0 else 0
        
# #         st.metric("🎯 Overall Compliance Rate", f"{overall_compliance:.1f}%")
# #         st.metric("👥 Total Participating Farms", total_participants)
# #         st.metric("✅ Total Complied Farms", total_complied)
    
# #     with col2:
# #         # Best and worst performing groups
# #         if not compliance_df.empty:
# #             best_group = compliance_df.loc[compliance_df['Compliance Rate (%)'].idxmax()]
# #             worst_group = compliance_df.loc[compliance_df['Compliance Rate (%)'].idxmin()]
            
# #             st.success(f"🏆 Best Compliance: {best_group['Study Group']} ({best_group['Compliance Rate (%)']}%)")
# #             st.error(f"⚠️ Lowest Compliance: {worst_group['Study Group']} ({worst_group['Compliance Rate (%)']}%)")

# # def create_comprehensive_downloads(merged_df, kharif_df, farm_daily_avg, weekly_avg):
# #     """Create comprehensive download section with all data exports"""
    
# #     st.markdown('<div class="section-header">💾 Comprehensive Data Downloads</div>', unsafe_allow_html=True)
    
# #     st.markdown("### 📋 Available Data Exports")
    
# #     col1, col2, col3 = st.columns(3)
    
# #     with col1:
# #         st.markdown("**📊 Complete Datasets**")
        
# #         # Complete merged dataset
# #         csv_buffer = io.StringIO()
# #         merged_df.to_csv(csv_buffer, index=False)
# #         st.download_button(
# #             label="📥 Complete Merged Dataset",
# #             data=csv_buffer.getvalue(),
# #             file_name="complete_merged_agricultural_data.csv",
# #             mime="text/csv",
# #             help="All water level data merged with farm information"
# #         )
        
# #         # Raw Kharif data
# #         csv_buffer = io.StringIO()
# #         kharif_df.to_csv(csv_buffer, index=False)
# #         st.download_button(
# #             label="📥 Raw Kharif Data",
# #             data=csv_buffer.getvalue(),
# #             file_name="raw_kharif_farm_data.csv",
# #             mime="text/csv",
# #             help="Original farm and study group data"
# #         )
    
# #     with col2:
# #         st.markdown("**👥 Study Group Data**")
        
# #         # Create study group datasets
# #         study_groups = create_study_group_datasets(merged_df, kharif_df)
        
# #         for group_name, group_data in study_groups.items():
# #             if not group_data.empty:
# #                 csv_buffer = io.StringIO()
# #                 group_data.to_csv(csv_buffer, index=False)
# #                 st.download_button(
# #                     label=f"📥 {group_name}",
# #                     data=csv_buffer.getvalue(),
# #                     file_name=f"{group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}_data.csv",
# #                     mime="text/csv",
# #                     help=f"Data for {group_name} participants"
# #                 )
    
# #     with col3:
# #         st.markdown("**📈 Analysis Reports**")
        
# #         # Village summary
# #         if 'Village' in merged_df.columns:
# #             village_summary = merged_df.groupby('Village').agg({
# #                 'Water Level (mm)': ['mean', 'std', 'count'],
# #                 'Farm ID': 'nunique'
# #             }).round(2)
# #             village_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Unique Farms']
            
# #             csv_buffer = io.StringIO()
# #             village_summary.to_csv(csv_buffer)
# #             st.download_button(
# #                 label="📥 Village Summary",
# #                 data=csv_buffer.getvalue(),
# #                 file_name="village_summary_report.csv",
# #                 mime="text/csv",
# #                 help="Statistical summary by village"
# #             )
        
# #         # Farm summary
# #         farm_summary = merged_df.groupby('Farm ID').agg({
# #             'Water Level (mm)': ['mean', 'std', 'count'],
# #             'Days from TPR': ['min', 'max']
# #         }).round(2)
# #         farm_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Min Days', 'Max Days']
        
# #         csv_buffer = io.StringIO()
# #         farm_summary.to_csv(csv_buffer)
# #         st.download_button(
# #             label="📥 Farm Summary",
# #             data=csv_buffer.getvalue(),
# #             file_name="farm_summary_report.csv",
# #             mime="text/csv",
# #             help="Statistical summary by farm"
# #         )
    
# #     # Create comprehensive ZIP download
# #     st.markdown("### 📦 Complete Data Package")
# #     st.markdown("*Download all datasets and reports in a single ZIP file*")
    
# #     if st.button("🗜️ Generate Complete Data Package", help="Create ZIP file with all data"):
# #         create_zip_package(merged_df, kharif_df, farm_daily_avg, weekly_avg)

# # def create_study_group_datasets(merged_df, kharif_df):
# #     """Create datasets for each study group"""
    
# #     # Merge for study group classifications
# #     study_data = pd.merge(
# #         merged_df,
# #         kharif_df[[
# #             'Kharif 25 Farm ID',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
# #             'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
# #             'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group B -training only (Y/N)',
# #             'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - Control (Y/N)',
# #             'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
# #             'Kharif 25 - TPR Group Study (Y/N)',
# #             'Kharif 25 - DSR farm Study (Y/N)'
# #         ]],
# #         left_on='Farm ID',
# #         right_on='Kharif 25 Farm ID',
# #         how='left'
# #     )
    
# #     study_groups = {}
    
# #     # Remote Controllers groups
# #     rc_treatment = study_data[study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'] == 1]
# #     if not rc_treatment.empty:
# #         study_groups['Remote Controllers Treatment'] = rc_treatment
    
# #     rc_control = study_data[study_data['Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'] == 1]
# #     if not rc_control.empty:
# #         study_groups['Remote Controllers Control'] = rc_control
    
# #     # AWD groups
# #     awd_a = study_data[study_data['Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'] == 1]
# #     if not awd_a.empty:
# #         study_groups['AWD Group A Treatment'] = awd_a
    
# #     awd_b = study_data[study_data['Kharif 25 - AWD Study - Group B - Complied (Y/N)'] == 1]
# #     if not awd_b.empty:
# #         study_groups['AWD Group B Training'] = awd_b
    
# #     awd_c = study_data[study_data['Kharif 25 - AWD Study - Group C - Complied (Y/N)'] == 1]
# #     if not awd_c.empty:
# #         study_groups['AWD Group C Control'] = awd_c
    
# #     # Farming methods
# #     dsr_group = study_data[study_data['Kharif 25 - DSR farm Study (Y/N)'] == 1]
# #     if not dsr_group.empty:
# #         study_groups['DSR Farms'] = dsr_group
    
# #     tpr_group = study_data[study_data['Kharif 25 - TPR Group Study (Y/N)'] == 1]
# #     if not tpr_group.empty:
# #         study_groups['TPR Farms'] = tpr_group
    
# #     return study_groups

# # def create_zip_package(merged_df, kharif_df, farm_daily_avg, weekly_avg):
# #     """Create comprehensive ZIP package with all data"""
    
# #     zip_buffer = io.BytesIO()
    
# #     with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        
# #         # Add main datasets
# #         csv_buffer = io.StringIO()
# #         merged_df.to_csv(csv_buffer, index=False)
# #         zip_file.writestr("01_complete_merged_data.csv", csv_buffer.getvalue())
        
# #         csv_buffer = io.StringIO()
# #         kharif_df.to_csv(csv_buffer, index=False)
# #         zip_file.writestr("02_raw_kharif_data.csv", csv_buffer.getvalue())
        
# #         # Add processed datasets
# #         if not farm_daily_avg.empty:
# #             csv_buffer = io.StringIO()
# #             farm_daily_avg.to_csv(csv_buffer, index=False)
# #             zip_file.writestr("03_farm_daily_averages.csv", csv_buffer.getvalue())
        
# #         if not weekly_avg.empty:
# #             csv_buffer = io.StringIO()
# #             weekly_avg.to_csv(csv_buffer, index=False)
# #             zip_file.writestr("04_weekly_averages.csv", csv_buffer.getvalue())
        
# #         # Add study group datasets
# #         study_groups = create_study_group_datasets(merged_df, kharif_df)
# #         for i, (group_name, group_data) in enumerate(study_groups.items(), 5):
# #             if not group_data.empty:
# #                 csv_buffer = io.StringIO()
# #                 group_data.to_csv(csv_buffer, index=False)
# #                 filename = f"{i:02d}_{group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.csv"
# #                 zip_file.writestr(filename, csv_buffer.getvalue())
        
# #         # Add summary reports
# #         if 'Village' in merged_df.columns:
# #             village_summary = merged_df.groupby('Village').agg({
# #                 'Water Level (mm)': ['mean', 'std', 'count'],
# #                 'Farm ID': 'nunique'
# #             }).round(2)
# #             village_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Unique Farms']
            
# #             csv_buffer = io.StringIO()
# #             village_summary.to_csv(csv_buffer)
# #             zip_file.writestr("20_village_summary.csv", csv_buffer.getvalue())
        
# #         farm_summary = merged_df.groupby('Farm ID').agg({
# #             'Water Level (mm)': ['mean', 'std', 'count'],
# #             'Days from TPR': ['min', 'max']
# #         }).round(2)
# #         farm_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Min Days', 'Max Days']
        
# #         csv_buffer = io.StringIO()
# #         farm_summary.to_csv(csv_buffer)
# #         zip_file.writestr("21_farm_summary.csv", csv_buffer.getvalue())
        
# #         # Add README
# #         readme_content = """
# # Agricultural Data Analysis Package
# # =================================

# # This package contains:

# # Main Datasets:
# # - 01_complete_merged_data.csv: All water level data merged with farm information
# # - 02_raw_kharif_data.csv: Original farm and study group data
# # - 03_farm_daily_averages.csv: Daily averages per farm
# # - 04_weekly_averages.csv: Weekly averages per farm

# # Study Groups:
# # - Remote Controllers Treatment/Control groups
# # - AWD Study Groups A, B, C
# # - DSR and TPR farming method groups

# # Summary Reports:
# # - 20_village_summary.csv: Statistics by village
# # - 21_farm_summary.csv: Statistics by farm

# # Generated on: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
# #         zip_file.writestr("README.txt", readme_content)
    
# #     zip_buffer.seek(0)
    
# #     st.download_button(
# #         label="📦 Download Complete Package (ZIP)",
# #         data=zip_buffer.getvalue(),
# #         file_name=f"agricultural_data_complete_package_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
# #         mime="application/zip",
# #         help="Complete package with all datasets and reports"
# #     )

# # def main():
# #     """Enhanced main function with complete dashboard functionality"""
    
# #     # Main title
# #     st.markdown('<div class="main-header">🌾 Enhanced Agricultural Data Analysis Dashboard</div>', unsafe_allow_html=True)
# #     st.markdown("*Comprehensive analysis with advanced filtering, comparisons, and enhanced downloads*")
    
# #     # Add navigation to 2024 analysis
# #     col1, col2, col3 = st.columns([1, 2, 1])
# #     with col2:
# #         st.link_button("🔗 Analyze 2024 Data", "https://v45bgthcmmrztmbstkddra.streamlit.app/", use_container_width=True)
    
# #     st.markdown("---")
    
# #     # Load and validate data
# #     kharif_df, water_df = load_and_validate_data()
    
# #     if kharif_df is not None and water_df is not None:
        
# #         # Data processing with progress indicator
# #         with st.spinner("🔄 Processing and cleaning data..."):
# #             kharif_cleaned, water_cleaned = clean_and_process_data(kharif_df, water_df)
            
# #             # Create filters
# #             filters = create_advanced_filters(kharif_cleaned, water_cleaned)
            
# #             # Apply filters
# #             filtered_kharif, filtered_water = apply_comprehensive_filters(kharif_cleaned, water_cleaned, filters)
            
# #             # Create merged dataset
# #             merged_df, farm_daily_avg, weekly_avg = create_merged_dataset(filtered_kharif, filtered_water)
        
# #         # Display data overview in sidebar
# #         with st.sidebar:
# #             st.markdown('<div class="section-header">📊 Data Overview</div>', unsafe_allow_html=True)
            
# #             st.markdown(f"""
# #             **📈 Current Dataset:**
# #             - **Merged Records:** {len(merged_df):,}
# #             - **Unique Farms:** {merged_df['Farm ID'].nunique() if not merged_df.empty else 0:,}
# #             - **Villages:** {merged_df['Village'].nunique() if 'Village' in merged_df.columns and not merged_df.empty else 0:,}
# #             - **Date Range:** {merged_df['Date'].min().strftime('%Y-%m-%d') if not merged_df.empty else 'N/A'} to {merged_df['Date'].max().strftime('%Y-%m-%d') if not merged_df.empty else 'N/A'}
# #             """)
            
# #             if not merged_df.empty:
# #                 avg_water_level = merged_df['Water Level (mm)'].mean()
# #                 st.markdown(f"- **Avg Water Level:** {avg_water_level:.1f} mm")
            
# #             st.markdown("---")
# #             st.markdown("**📋 Original Data:**")
# #             st.markdown(f"- **Kharif Records:** {len(kharif_df):,}")
# #             st.markdown(f"- **Water Records:** {len(water_df):,}")
        
# #         if merged_df.empty:
# #             st.warning("⚠️ No data available after applying filters. Please adjust your filter settings.")
            
# #             with st.expander("🔧 Troubleshooting Tips"):
# #                 st.markdown("""
# #                 **Common Issues:**
# #                 - **Date Range:** Ensure selected dates overlap with your data
# #                 - **Village Names:** Check for typos or variations in village names
# #                 - **Study Groups:** Verify that selected groups have data
# #                 - **Farm IDs:** Ensure farm IDs match between datasets
                
# #                 **Try:**
# #                 - Reset filters to "All" options
# #                 - Check the original data structure
# #                 - Expand date range selection
# #                 """)
# #         else:
# #             st.success(f"✅ Successfully processed {len(merged_df):,} records from {merged_df['Farm ID'].nunique()} farms!")
            
# #             # Create main tabs
# #             tab1, tab2, tab3 = st.tabs([
# #                 "🏡 Individual Farm Analysis",
# #                 "👥 Comparative Analysis",
# #                 "💾 Data Downloads"
# #             ])
            
# #             with tab1:
# #                 render_individual_farm_analysis(merged_df, farm_daily_avg, weekly_avg)
            
# #             with tab2:
# #                 render_comparative_analysis(merged_df, filtered_kharif)
            
# #             with tab3:
# #                 create_comprehensive_downloads(merged_df, filtered_kharif, farm_daily_avg, weekly_avg)
    
# #     else:
# #         # Data upload instructions
# #         st.info("📁 Please upload both Excel files to begin analysis.")
        
# #         with st.expander("ℹ️ Expected Data Structure & Features", expanded=True):
# #             st.markdown("""
# #             ### 📋 Required Files:
            
# #             **1. Kharif 25 Excel File:**
# #             - `Kharif 25 Farm ID` - Unique farm identifier
# #             - `Kharif 25 Village` - Village name
# #             - `Kharif 25 Paddy transplanting date (TPR)` - Transplanting date
# #             - Study group columns (Remote Controllers, AWD, TPR, DSR)
# #             - PVC Pipe codes (1-5)
# #             - Compliance indicators (Y/N)
            
# #             **2. Water Level Measurement Excel File:**
# #             - `Date` - Measurement date
# #             - `Farm ID` - Farm identifier (must match Kharif file)
# #             - `Pipe code ID of the farm` - Pipe identifier
# #             - `Measure water level inside the PVC pipe - millimeter mm` - Water level reading
# #             - `Village name` - Village name
            
# #             ### ✨ Enhanced Features:
            
# #             **🔍 Advanced Filters:**
# #             - 📅 Date range selection with validation
# #             - 🏘️ Village-specific filtering with typo handling
# #             - 🔬 Study group filtering (RC, AWD, TPR, DSR)
# #             - ✅ Compliance status filtering
# #             - 🔧 Data quality filters (minimum readings, outlier removal)
            
# #             **📊 Complete Analysis:**
# #             - **Graph 1:** Daily water levels per pipe + farm average (markers only)
# #             - **Graph 2:** Weekly water level trends (markers + farm average line)
# #             - **Table 3:** Water level data with Days from TPR as Column A
# #             - **Comparative Charts:** All required study group comparisons
            
# #             **👥 Study Group Comparisons:**
# #             - Remote Controllers: Treatment vs Control (complied groups)
# #             - AWD Study: Groups A, B, C (complied and non-complied)
# #             - DSR vs TPR group comparisons
# #             - Village-level aggregations
# #             - Comprehensive compliance analysis
            
# #             **💾 Enhanced Downloads:**
# #             - Individual farm reports (detailed + summary)
# #             - Study group datasets (separate CSV files)
# #             - Village and farm summary reports
# #             - Complete data packages (ZIP format)
            
# #             **🔧 Data Quality Features:**
# #             - Fuzzy matching for village names (handles typos)
# #             - Case insensitive comparisons
# #             - Data normalization and cleaning
# #             - Outlier detection and removal
# #             - Missing data handling
            
# #             **📈 Advanced Visualizations:**
# #             - Interactive charts with hover information
# #             - Color-coded study groups
# #             - Responsive design for all screen sizes
# #             - Export-ready chart formats
# #             """)

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta
# import plotly.graph_objects as go
# import plotly.express as px
# import io
# import re
# import zipfile
# import warnings
# warnings.filterwarnings('ignore')

# # Configure page
# st.set_page_config(
#     page_title="Enhanced Agricultural Data Analysis Dashboard",
#     page_icon="🌾",
#     layout="wide"
# )

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     .main-header {
#         font-size: 2.5rem;
#         color: #2E7D32;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .section-header {
#         font-size: 1.5rem;
#         color: #1976D2;
#         border-bottom: 2px solid #1976D2;
#         padding-bottom: 0.5rem;
#         margin: 1.5rem 0 1rem 0;
#     }
#     .metric-container {
#         background-color: #f0f2f6;
#         padding: 1rem;
#         border-radius: 0.5rem;
#         margin: 0.5rem 0;
#     }
#     .filter-section {
#         background-color: #e8f5e8;
#         padding: 1rem;
#         border-radius: 0.5rem;
#         margin-bottom: 1rem;
#     }
#     .debug-info {
#         background-color: #f8f9fa;
#         padding: 0.5rem;
#         border-radius: 0.25rem;
#         border-left: 4px solid #17a2b8;
#         margin: 0.5rem 0;
#         font-size: 0.8rem;
#     }
# </style>
# """, unsafe_allow_html=True)

# def normalize_text(text):
#     """Normalize text for consistent comparison"""
#     if pd.isna(text) or text is None:
#         return ""
#     text = str(text).strip().lower()
#     text = re.sub(r'\s+', ' ', text)
#     text = re.sub(r'[^\w\s]', '', text)
#     return text

# def fuzzy_match_villages(village_list, threshold=85):
#     """Group similar village names using simple similarity"""
#     if not village_list:
#         return []
    
#     normalized_villages = {}
#     for village in village_list:
#         if pd.isna(village):
#             continue
        
#         norm_village = normalize_text(village)
#         if not norm_village:
#             continue
            
#         # Check for exact matches first
#         found_match = False
#         for existing_norm, original in normalized_villages.items():
#             if norm_village == existing_norm:
#                 found_match = True
#                 break
#             # Simple similarity check
#             if len(norm_village) > 3 and len(existing_norm) > 3:
#                 if norm_village in existing_norm or existing_norm in norm_village:
#                     found_match = True
#                     break
        
#         if not found_match:
#             normalized_villages[norm_village] = str(village).strip()
    
#     return sorted(list(normalized_villages.values()))

# def convert_binary_column(series):
#     """Convert Y/N, Yes/No, 1/0 to consistent 1/0 format"""
#     if series.dtype == 'object':
#         # Handle string values
#         return series.apply(lambda x: 1 if str(x).upper().strip() in ['Y', 'YES', '1', 'TRUE'] else 0)
#     else:
#         # Handle numeric values
#         return series.apply(lambda x: 1 if pd.notna(x) and (x == 1 or x == '1') else 0)

# def load_and_validate_data():
#     """Load and validate uploaded Excel files"""
#     st.markdown('<div class="section-header">📁 Data Upload Section</div>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("**Upload Kharif 25 Excel File**")
#         kharif_file = st.file_uploader(
#             "Choose Kharif file", 
#             type=['xlsx', 'xls'],
#             help="Upload the main farm data file with study group information"
#         )
#         if kharif_file:
#             st.success("✅ Kharif file uploaded successfully")
    
#     with col2:
#         st.markdown("**Upload Water Level Excel File**")
#         water_file = st.file_uploader(
#             "Choose Water Level file", 
#             type=['xlsx', 'xls'],
#             help="Upload the water level measurement data file"
#         )
#         if water_file:
#             st.success("✅ Water level file uploaded successfully")
    
#     if kharif_file is not None and water_file is not None:
#         try:
#             with st.spinner("📊 Loading and validating data..."):
#                 # Load data
#                 kharif_df = pd.read_excel(kharif_file)
#                 water_df = pd.read_excel(water_file)
                
#                 # Validate required columns
#                 required_kharif_cols = [
#                     'Kharif 25 Farm ID',
#                     'Kharif 25 Village',
#                     'Kharif 25 Paddy transplanting date (TPR)'
#                 ]
                
#                 required_water_cols = [
#                     'Date',
#                     'Farm ID',
#                     'Pipe code ID of the farm',
#                     'Measure water level inside the PVC pipe - millimeter mm'
#                 ]
                
#                 missing_kharif = [col for col in required_kharif_cols if col not in kharif_df.columns]
#                 missing_water = [col for col in required_water_cols if col not in water_df.columns]
                
#                 if missing_kharif:
#                     st.error(f"❌ Missing columns in Kharif file: {missing_kharif}")
#                     return None, None
                
#                 if missing_water:
#                     st.error(f"❌ Missing columns in Water file: {missing_water}")
#                     return None, None
                
#                 st.success("✅ Data validation completed successfully!")
#                 return kharif_df, water_df
                
#         except Exception as e:
#             st.error(f"❌ Error loading files: {str(e)}")
#             return None, None
    
#     return None, None

# def clean_and_process_data(kharif_df, water_df):
#     """Enhanced data cleaning and processing"""
    
#     kharif_cleaned = kharif_df.copy()
#     water_cleaned = water_df.copy()
    
#     # Clean and normalize text columns
#     if 'Kharif 25 Village' in kharif_cleaned.columns:
#         kharif_cleaned['Village_Normalized'] = kharif_cleaned['Kharif 25 Village'].apply(lambda x: normalize_text(x) if pd.notna(x) else "")
#         kharif_cleaned['Kharif 25 Village'] = kharif_cleaned['Kharif 25 Village'].astype(str).str.strip()
    
#     if 'Village name' in water_cleaned.columns:
#         water_cleaned['Village_Normalized'] = water_cleaned['Village name'].apply(lambda x: normalize_text(x) if pd.notna(x) else "")
#         water_cleaned['Village name'] = water_cleaned['Village name'].astype(str).str.strip()
    
#     # Clean Farm IDs
#     if 'Farm ID' in water_cleaned.columns:
#         water_cleaned['Farm ID'] = water_cleaned['Farm ID'].astype(str).str.strip().str.upper()
    
#     if 'Kharif 25 Farm ID' in kharif_cleaned.columns:
#         kharif_cleaned['Kharif 25 Farm ID'] = kharif_cleaned['Kharif 25 Farm ID'].astype(str).str.strip().str.upper()
    
#     # Handle dates properly
#     if 'Date' in water_cleaned.columns:
#         water_cleaned['Date'] = pd.to_datetime(water_cleaned['Date'], errors='coerce')
#         water_cleaned = water_cleaned.dropna(subset=['Date'])
    
#     if 'Kharif 25 Paddy transplanting date (TPR)' in kharif_cleaned.columns:
#         kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'] = pd.to_datetime(
#             kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'], errors='coerce'
#         )
#         # Fill missing TPR dates with June 1, 2025
#         kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'].fillna(
#             pd.Timestamp('2025-06-01'), inplace=True
#         )
    
#     # Clean water level measurements
#     if 'Measure water level inside the PVC pipe - millimeter mm' in water_cleaned.columns:
#         water_cleaned['Water_Level_Numeric'] = pd.to_numeric(
#             water_cleaned['Measure water level inside the PVC pipe - millimeter mm'], 
#             errors='coerce'
#         )
#         water_cleaned = water_cleaned.dropna(subset=['Water_Level_Numeric'])
    
#     # Handle binary columns (Y/N to 1/0) - IMPROVED LOGIC
#     binary_columns = [col for col in kharif_cleaned.columns if '(Y/N)' in col]
    
#     if binary_columns:
#         st.info(f"🔧 Processing {len(binary_columns)} binary columns for study groups...")
        
#     for col in binary_columns:
#         if col in kharif_cleaned.columns:
#             original_values = kharif_cleaned[col].value_counts()
#             kharif_cleaned[col] = convert_binary_column(kharif_cleaned[col])
            
#             # Debug info for binary conversion
#             converted_count = kharif_cleaned[col].sum()
#             if converted_count > 0:
#                 st.sidebar.success(f"✅ {col.split(' - ')[-1]}: {converted_count} farms")
    
#     return kharif_cleaned, water_cleaned

# def get_available_study_groups(kharif_df):
#     """Get available study groups and their counts"""
#     study_groups = {}
    
#     # Remote Controllers Study
#     rc_cols = {
#         'Treatment Group (A)': 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
#         'Treatment Complied (A)': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
#         'Treatment Non-Complied (A)': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
#         'Control Group (B)': 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
#         'Control Complied (B)': 'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
#         'Control Non-Complied (B)': 'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)'
#     }
    
#     for group_name, col_name in rc_cols.items():
#         if col_name in kharif_df.columns:
#             count = kharif_df[col_name].sum() if kharif_df[col_name].dtype in ['int64', 'float64'] else 0
#             if count > 0:
#                 study_groups[f"RC - {group_name}"] = {'column': col_name, 'count': count}
    
#     # AWD Study
#     awd_cols = {
#         'Group A Treatment': 'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
#         'Group A Complied': 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
#         'Group A Non-Complied': 'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
#         'Group B Training': 'Kharif 25 - AWD Study - Group B -training only (Y/N)',
#         'Group B Complied': 'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
#         'Group B Non-Complied': 'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
#         'Group C Control': 'Kharif 25 - AWD Study - Group C - Control (Y/N)',
#         'Group C Complied': 'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
#         'Group C Non-Complied': 'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
#     }
    
#     for group_name, col_name in awd_cols.items():
#         if col_name in kharif_df.columns:
#             count = kharif_df[col_name].sum() if kharif_df[col_name].dtype in ['int64', 'float64'] else 0
#             if count > 0:
#                 study_groups[f"AWD - {group_name}"] = {'column': col_name, 'count': count}
    
#     # Farming Methods
#     farming_cols = {
#         'TPR Group': 'Kharif 25 - TPR Group Study (Y/N)',
#         'DSR Group': 'Kharif 25 - DSR farm Study (Y/N)'
#     }
    
#     for group_name, col_name in farming_cols.items():
#         if col_name in kharif_df.columns:
#             count = kharif_df[col_name].sum() if kharif_df[col_name].dtype in ['int64', 'float64'] else 0
#             if count > 0:
#                 study_groups[group_name] = {'column': col_name, 'count': count}
    
#     return study_groups

# def create_advanced_filters(kharif_df, water_df):
#     """Create comprehensive filtering system with improved study group detection"""
    
#     st.sidebar.markdown('<div class="section-header">🔍 Advanced Filters</div>', unsafe_allow_html=True)
    
#     filters = {}
    
#     # Date Range Filter
#     with st.sidebar.expander("📅 Date Range Filter", expanded=True):
#         if 'Date' in water_df.columns and not water_df['Date'].isna().all():
#             min_date = water_df['Date'].min().date()
#             max_date = water_df['Date'].max().date()
            
#             date_range = st.date_input(
#                 "Select date range:",
#                 value=(min_date, max_date),
#                 min_value=min_date,
#                 max_value=max_date
#             )
            
#             if len(date_range) == 2:
#                 filters['date_range'] = date_range
#                 st.info(f"📊 Selected: {date_range[0]} to {date_range[1]}")
    
#     # Village Filter
#     with st.sidebar.expander("🏘️ Village Filter", expanded=True):
#         villages = []
#         if 'Kharif 25 Village' in kharif_df.columns:
#             villages.extend(kharif_df['Kharif 25 Village'].dropna().unique())
#         if 'Village name' in water_df.columns:
#             villages.extend(water_df['Village name'].dropna().unique())
        
#         unique_villages = fuzzy_match_villages(list(set(villages)))
        
#         selected_villages = st.multiselect(
#             "Select villages:",
#             options=unique_villages,
#             default=[],
#             help="Select specific villages to analyze"
#         )
#         filters['villages'] = selected_villages
        
#         if selected_villages:
#             st.info(f"📍 Selected {len(selected_villages)} village(s)")
    
#     # Study Group Filters - IMPROVED
#     with st.sidebar.expander("🔬 Study Group Filters", expanded=True):
        
#         # Get available study groups
#         available_groups = get_available_study_groups(kharif_df)
        
#         if available_groups:
#             st.markdown("**Available Study Groups:**")
            
#             # Show available groups with counts
#             for group_name, group_info in available_groups.items():
#                 st.markdown(f"• {group_name}: {group_info['count']} farms")
            
#             st.markdown("---")
            
#             # Remote Controllers Study
#             st.markdown("**Remote Controllers Study:**")
#             rc_options = ["All"] + [name for name in available_groups.keys() if name.startswith("RC -")]
#             rc_filter = st.selectbox(
#                 "RC Group:",
#                 options=rc_options,
#                 help="Filter by Remote Controllers study groups"
#             )
#             filters['remote_controllers'] = rc_filter
            
#             # AWD Study
#             st.markdown("**AWD Study:**")
#             awd_options = ["All"] + [name for name in available_groups.keys() if name.startswith("AWD -")]
#             awd_filter = st.selectbox(
#                 "AWD Group:",
#                 options=awd_options,
#                 help="Filter by AWD study groups"
#             )
#             filters['awd_study'] = awd_filter
            
#             # Farming Method
#             st.markdown("**Farming Method:**")
#             farming_options = ["All"] + [name for name in available_groups.keys() if name in ["TPR Group", "DSR Group"]]
#             farming_method = st.selectbox(
#                 "Method:",
#                 options=farming_options,
#                 help="Filter by farming method"
#             )
#             filters['farming_method'] = farming_method
            
#             # Store available groups for filter application
#             filters['available_groups'] = available_groups
            
#         else:
#             st.warning("⚠️ No study groups detected. Check if binary columns contain valid data.")
    
#     # Data Quality Filters
#     with st.sidebar.expander("🔧 Data Quality", expanded=False):
        
#         min_readings = st.number_input(
#             "Min readings per farm:",
#             min_value=1,
#             max_value=100,
#             value=1,
#             help="Minimum number of water level readings per farm"
#         )
#         filters['min_readings'] = min_readings
        
#         outlier_filter = st.checkbox(
#             "Remove outliers",
#             value=False,
#             help="Remove statistical outliers from water level data"
#         )
#         filters['remove_outliers'] = outlier_filter
    
#     return filters

# def apply_comprehensive_filters(kharif_df, water_df, filters):
#     """Apply all selected filters to the datasets - IMPROVED"""
    
#     filtered_kharif = kharif_df.copy()
#     filtered_water = water_df.copy()
    
#     # Apply date filter
#     if 'date_range' in filters and len(filters['date_range']) == 2:
#         start_date, end_date = filters['date_range']
#         filtered_water = filtered_water[
#             (filtered_water['Date'] >= pd.Timestamp(start_date)) &
#             (filtered_water['Date'] <= pd.Timestamp(end_date))
#         ]
    
#     # Apply village filter
#     if filters['villages']:
#         # Normalize selected villages for comparison
#         normalized_selected = [normalize_text(v) for v in filters['villages']]
        
#         if 'Village_Normalized' in filtered_kharif.columns:
#             filtered_kharif = filtered_kharif[
#                 filtered_kharif['Village_Normalized'].isin(normalized_selected)
#             ]
        
#         if 'Village_Normalized' in filtered_water.columns:
#             filtered_water = filtered_water[
#                 filtered_water['Village_Normalized'].isin(normalized_selected)
#             ]
    
#     # Apply study group filters - IMPROVED LOGIC
#     available_groups = filters.get('available_groups', {})
    
#     # Remote Controllers filter
#     if filters.get('remote_controllers', 'All') != "All":
#         selected_group = filters['remote_controllers']
#         if selected_group in available_groups:
#             column_name = available_groups[selected_group]['column']
#             mask = filtered_kharif[column_name] == 1
#             filtered_kharif = filtered_kharif[mask]
            
#             # Debug info
#             st.sidebar.success(f"✅ Applied RC filter: {mask.sum()} farms selected")
    
#     # AWD filter
#     if filters.get('awd_study', 'All') != "All":
#         selected_group = filters['awd_study']
#         if selected_group in available_groups:
#             column_name = available_groups[selected_group]['column']
#             mask = filtered_kharif[column_name] == 1
#             filtered_kharif = filtered_kharif[mask]
            
#             # Debug info
#             st.sidebar.success(f"✅ Applied AWD filter: {mask.sum()} farms selected")
    
#     # Farming method filter
#     if filters.get('farming_method', 'All') != "All":
#         selected_group = filters['farming_method']
#         if selected_group in available_groups:
#             column_name = available_groups[selected_group]['column']
#             mask = filtered_kharif[column_name] == 1
#             filtered_kharif = filtered_kharif[mask]
            
#             # Debug info
#             st.sidebar.success(f"✅ Applied farming method filter: {mask.sum()} farms selected")
    
#     # Apply minimum readings filter
#     if 'min_readings' in filters and filters['min_readings'] > 1:
#         farm_counts = filtered_water['Farm ID'].value_counts()
#         valid_farms = farm_counts[farm_counts >= filters['min_readings']].index
#         filtered_water = filtered_water[filtered_water['Farm ID'].isin(valid_farms)]
    
#     # Apply outlier removal
#     if filters.get('remove_outliers', False) and 'Water_Level_Numeric' in filtered_water.columns:
#         Q1 = filtered_water['Water_Level_Numeric'].quantile(0.25)
#         Q3 = filtered_water['Water_Level_Numeric'].quantile(0.75)
#         IQR = Q3 - Q1
#         lower_bound = Q1 - 1.5 * IQR
#         upper_bound = Q3 + 1.5 * IQR
        
#         filtered_water = filtered_water[
#             (filtered_water['Water_Level_Numeric'] >= lower_bound) &
#             (filtered_water['Water_Level_Numeric'] <= upper_bound)
#         ]
    
#     return filtered_kharif, filtered_water

# def create_merged_dataset(kharif_df, water_df):
#     """Create comprehensive merged dataset with all calculations"""
    
#     # Select relevant columns for merging
#     kharif_cols = [
#         "Kharif 25 Farm ID",
#         "Kharif 25 Village",
#         "Kharif 25 Paddy transplanting date (TPR)"
#     ]
    
#     # Add pipe code columns if they exist
#     for i in range(1, 6):
#         pipe_col = f"Kharif 25 PVC Pipe code - {i}"
#         if pipe_col in kharif_df.columns:
#             kharif_cols.append(pipe_col)
    
#     kharif_subset = kharif_df[kharif_cols].copy()
    
#     # Select water level columns
#     water_cols = [
#         "Date",
#         "Farm ID",
#         "Village name",
#         "Pipe code ID of the farm"
#     ]
    
#     # Handle different possible column names for water level
#     water_level_col = None
#     possible_water_cols = [
#         "Measure water level inside the PVC pipe - millimeter mm",
#         "Water_Level_Numeric",
#         "Water Level (mm)"
#     ]
    
#     for col in possible_water_cols:
#         if col in water_df.columns:
#             water_level_col = col
#             break
    
#     if water_level_col:
#         water_cols.append(water_level_col)
    
#     water_subset = water_df[water_cols].copy()
    
#     # Merge datasets
#     merged_df = pd.merge(
#         water_subset,
#         kharif_subset,
#         how="inner",
#         left_on="Farm ID",
#         right_on="Kharif 25 Farm ID"
#     )
    
#     # Rename columns for clarity
#     column_renames = {
#         water_level_col: "Water Level (mm)",
#         "Kharif 25 Paddy transplanting date (TPR)": "TPR Date",
#         "Kharif 25 Village": "Village"
#     }
    
#     merged_df.rename(columns=column_renames, inplace=True)
    
#     # Calculate days and weeks from TPR
#     if 'TPR Date' in merged_df.columns and 'Date' in merged_df.columns:
#         merged_df["Days from TPR"] = (merged_df["Date"] - merged_df["TPR Date"]).dt.days
#         merged_df["Week from TPR"] = (merged_df["Days from TPR"] / 7).astype(int)
    
#     # Calculate farm-level daily averages
#     if 'Water Level (mm)' in merged_df.columns:
#         farm_daily_avg = merged_df.groupby(['Farm ID', 'Date']).agg({
#             'Water Level (mm)': 'mean',
#             'TPR Date': 'first',
#             'Village': 'first'
#         }).reset_index()
        
#         farm_daily_avg["Days from TPR"] = (farm_daily_avg["Date"] - farm_daily_avg["TPR Date"]).dt.days
#         farm_daily_avg["Week from TPR"] = (farm_daily_avg["Days from TPR"] / 7).astype(int)
        
#         # Calculate weekly averages
#         weekly_avg = merged_df.groupby(['Farm ID', 'Week from TPR']).agg({
#             'Water Level (mm)': 'mean',
#             'Village': 'first'
#         }).reset_index()
        
#         return merged_df, farm_daily_avg, weekly_avg
    
#     return merged_df, pd.DataFrame(), pd.DataFrame()

# def render_individual_farm_analysis(merged_df, farm_daily_avg, weekly_avg):
#     """Complete individual farm analysis with all required graphs and tables"""
    
#     st.markdown('<div class="section-header">🏡 Individual Farm Analysis</div>', unsafe_allow_html=True)
    
#     if merged_df.empty:
#         st.warning("⚠️ No data available for individual farm analysis. Please check your filters.")
#         return
    
#     # Farm selection with search
#     farm_ids = sorted(merged_df["Farm ID"].dropna().unique())
    
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         selected_farm = st.selectbox(
#             "🔍 Select Farm ID:",
#             options=farm_ids,
#             help="Choose a farm to analyze in detail"
#         )
    
#     with col2:
#         if selected_farm:
#             farm_info = merged_df[merged_df["Farm ID"] == selected_farm].iloc[0]
#             village = farm_info.get('Village', 'Unknown')
#             st.info(f"📍 Village: {village}")
    
#     if not selected_farm:
#         st.warning("Please select a farm ID to proceed.")
#         return
    
#     # Filter data for selected farm
#     farm_data = merged_df[merged_df["Farm ID"] == selected_farm].copy()
#     farm_daily_data = farm_daily_avg[farm_daily_avg["Farm ID"] == selected_farm].copy()
#     farm_weekly_data = weekly_avg[weekly_avg["Farm ID"] == selected_farm].copy()
    
#     if farm_data.empty:
#         st.warning(f"⚠️ No data found for Farm ID: {selected_farm}")
#         return
    
#     # Get available pipes
#     available_pipes = sorted(farm_data["Pipe code ID of the farm"].dropna().unique())
    
#     col1, col2 = st.columns([3, 1])
    
#     with col1:
#         selected_pipes = st.multiselect(
#             "🔧 Select Pipes to Analyze:",
#             options=available_pipes,
#             default=available_pipes[:3] if len(available_pipes) > 3 else available_pipes,
#             help="Choose which pipes to include in the analysis"
#         )
    
#     with col2:
#         st.metric("📊 Total Readings", len(farm_data))
#         st.metric("🔧 Available Pipes", len(available_pipes))
    
#     if not selected_pipes:
#         st.warning("⚠️ Please select at least one pipe to analyze.")
#         return
    
#     # Filter for selected pipes
#     filtered_farm_data = farm_data[farm_data["Pipe code ID of the farm"].isin(selected_pipes)].copy()
    
#     # **GRAPH 1: Daily Water Levels per Pipe + Farm Average**
#     st.markdown("### 📊 Graph 1: Daily Water Levels per Pipe + Farm Average")
    
#     fig1 = go.Figure()
    
#     # Color palette for pipes
#     colors = px.colors.qualitative.Set3
    
#     # Add each pipe as markers only
#     for i, pipe in enumerate(selected_pipes):
#         pipe_data = filtered_farm_data[filtered_farm_data["Pipe code ID of the farm"] == pipe].copy()
#         pipe_data = pipe_data.sort_values("Days from TPR")
        
#         fig1.add_trace(go.Scatter(
#             x=pipe_data["Days from TPR"],
#             y=pipe_data["Water Level (mm)"],
#             mode='markers',
#             name=f"Pipe {pipe}",
#             marker=dict(
#                 size=8,
#                 color=colors[i % len(colors)],
#                 opacity=0.7
#             ),
#             hovertemplate="<b>Pipe %{text}</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>",
#             text=[pipe] * len(pipe_data)
#         ))
    
#     # Add farm average as line + markers
#     if not farm_daily_data.empty:
#         farm_daily_sorted = farm_daily_data.sort_values("Days from TPR")
#         fig1.add_trace(go.Scatter(
#             x=farm_daily_sorted["Days from TPR"],
#             y=farm_daily_sorted["Water Level (mm)"],
#             mode='lines+markers',
#             name="Farm Average",
#             line=dict(width=4, color='black'),
#             marker=dict(symbol='diamond', size=12, color='black'),
#             hovertemplate="<b>Farm Average</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>"
#         ))
    
#     fig1.update_layout(
#         title=f"Daily Water Levels - Farm {selected_farm}",
#         xaxis_title="Days from Transplanting",
#         yaxis_title="PVC Water Level (mm)",
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         ),
#         hovermode="x unified",
#         height=500,
#         showlegend=True
#     )
    
#     st.plotly_chart(fig1, use_container_width=True)
    
#     # **GRAPH 2: Weekly Water Level Trends**
#     st.markdown("### 📈 Graph 2: Weekly Water Level Trends per Pipe + Farm Average")
    
#     fig2 = go.Figure()
    
#     # Weekly averages per pipe (markers only)
#     for i, pipe in enumerate(selected_pipes):
#         pipe_data = filtered_farm_data[filtered_farm_data["Pipe code ID of the farm"] == pipe]
#         pipe_weekly = pipe_data.groupby("Week from TPR")["Water Level (mm)"].mean().reset_index()
#         pipe_weekly = pipe_weekly.sort_values("Week from TPR")
        
#         fig2.add_trace(go.Scatter(
#             x=pipe_weekly["Week from TPR"],
#             y=pipe_weekly["Water Level (mm)"],
#             mode='markers',
#             name=f"Pipe {pipe}",
#             marker=dict(
#                 size=10,
#                 color=colors[i % len(colors)],
#                 opacity=0.7
#             ),
#             hovertemplate="<b>Pipe %{text}</b><br>" +
#                          "Week from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>",
#             text=[pipe] * len(pipe_weekly)
#         ))
    
#     # Farm weekly average (line + markers)
#     if not farm_weekly_data.empty:
#         farm_weekly_sorted = farm_weekly_data.sort_values("Week from TPR")
#         fig2.add_trace(go.Scatter(
#             x=farm_weekly_sorted["Week from TPR"],
#             y=farm_weekly_sorted["Water Level (mm)"],
#             mode='lines+markers',
#             name="Farm Weekly Average",
#             line=dict(width=4, color='black'),
#             marker=dict(symbol='diamond', size=12, color='black'),
#             hovertemplate="<b>Farm Weekly Average</b><br>" +
#                          "Week from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>"
#         ))
    
#     fig2.update_layout(
#         title=f"Weekly Water Level Trends - Farm {selected_farm}",
#         xaxis_title="Weeks from Transplanting",
#         yaxis_title="PVC Water Level (mm)",
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         ),
#         hovermode="x unified",
#         height=500,
#         showlegend=True
#     )
    
#     st.plotly_chart(fig2, use_container_width=True)
    
#     # **TABLE 3: Water Level Data (All Pipes) - As Required**
#     st.markdown("### 📋 Table 3: Water Level Data (All Pipes)")
#     st.markdown("*Individual pipe readings with timestamps and farm averages*")
    
#     # Create comprehensive table with Days from TPR as Column A
#     table_data = filtered_farm_data.pivot_table(
#         index="Days from TPR",
#         columns="Pipe code ID of the farm",
#         values="Water Level (mm)",
#         aggfunc='mean'
#     ).reset_index()
    
#     # Add farm average column
#     if not farm_daily_data.empty:
#         farm_avg_for_table = farm_daily_data.set_index("Days from TPR")["Water Level (mm)"]
#         table_data = table_data.set_index("Days from TPR")
#         table_data["Farm Average"] = farm_avg_for_table
#         table_data = table_data.reset_index()
    
#     # Add date column for timestamps
#     date_mapping = filtered_farm_data.groupby("Days from TPR")["Date"].first().reset_index()
#     table_data = pd.merge(table_data, date_mapping, on="Days from TPR", how="left")
    
#     # Reorder columns: Days from TPR (Column A), Date, Pipes, Farm Average
#     pipe_cols = [col for col in table_data.columns if col not in ["Days from TPR", "Date", "Farm Average"]]
#     column_order = ["Days from TPR", "Date"] + sorted(pipe_cols) + (["Farm Average"] if "Farm Average" in table_data.columns else [])
#     table_data = table_data[column_order]
    
#     # Format the table
#     st.dataframe(
#         table_data.style.format({
#             col: "{:.1f}" for col in table_data.columns if col not in ["Days from TPR", "Date"]
#         }).set_table_styles([
#             {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]},
#             {'selector': 'td', 'props': [('text-align', 'center')]}
#         ]),
#         use_container_width=True,
#         height=400
#     )
    
#     # Summary statistics
#     st.markdown("### 📊 Farm Summary Statistics")
    
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         avg_level = filtered_farm_data["Water Level (mm)"].mean()
#         st.metric("🌊 Average Water Level", f"{avg_level:.1f} mm")
    
#     with col2:
#         std_level = filtered_farm_data["Water Level (mm)"].std()
#         st.metric("📏 Standard Deviation", f"{std_level:.1f} mm")
    
#     with col3:
#         min_level = filtered_farm_data["Water Level (mm)"].min()
#         st.metric("⬇️ Minimum Level", f"{min_level:.1f} mm")
    
#     with col4:
#         max_level = filtered_farm_data["Water Level (mm)"].max()
#         st.metric("⬆️ Maximum Level", f"{max_level:.1f} mm")
    
#     # Download section for individual farm
#     st.markdown("### 💾 Download Individual Farm Data")
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         # Download detailed data
#         csv_buffer = io.StringIO()
#         filtered_farm_data.to_csv(csv_buffer, index=False)
#         st.download_button(
#             label="📥 Download Detailed Data",
#             data=csv_buffer.getvalue(),
#             file_name=f"farm_{selected_farm}_detailed_data.csv",
#             mime="text/csv",
#             help="All individual readings for this farm"
#         )
    
#     with col2:
#         # Download summary table
#         csv_buffer = io.StringIO()
#         table_data.to_csv(csv_buffer, index=False)
#         st.download_button(
#             label="📥 Download Summary Table",
#             data=csv_buffer.getvalue(),
#             file_name=f"farm_{selected_farm}_summary_table.csv",
#             mime="text/csv",
#             help="Table 3 data as shown above"
#         )
    
#     with col3:
#         # Download daily averages
#         if not farm_daily_data.empty:
#             csv_buffer = io.StringIO()
#             farm_daily_data.to_csv(csv_buffer, index=False)
#             st.download_button(
#                 label="📥 Download Daily Averages",
#                 data=csv_buffer.getvalue(),
#                 file_name=f"farm_{selected_farm}_daily_averages.csv",
#                 mime="text/csv",
#                 help="Farm daily average calculations"
#             )

# def render_comparative_analysis(merged_df, kharif_df):
#     """Comprehensive comparative analysis with all study group comparisons"""
    
#     st.markdown('<div class="section-header">👥 Comparative Analysis</div>', unsafe_allow_html=True)
    
#     if merged_df.empty:
#         st.warning("⚠️ No data available for comparative analysis. Please check your filters.")
#         return
    
#     # Analysis type selection
#     analysis_type = st.selectbox(
#         "📊 Select Analysis Type:",
#         options=[
#             "Village-level Aggregations",
#             "Remote Controllers: Treatment vs Control (Complied Groups)",
#             "AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)",
#             "DSR vs TPR Group Comparisons",
#             "Comprehensive Compliance Analysis"
#         ],
#         help="Choose the type of comparative analysis to perform"
#     )
    
#     if analysis_type == "Village-level Aggregations":
#         render_village_level_analysis(merged_df)
#     elif analysis_type == "Remote Controllers: Treatment vs Control (Complied Groups)":
#         render_remote_controllers_analysis(merged_df, kharif_df)
#     elif analysis_type == "AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)":
#         render_awd_groups_analysis(merged_df, kharif_df)
#     elif analysis_type == "DSR vs TPR Group Comparisons":
#         render_dsr_tpr_analysis(merged_df, kharif_df)
#     elif analysis_type == "Comprehensive Compliance Analysis":
#         render_compliance_analysis(merged_df, kharif_df)

# def render_village_level_analysis(merged_df):
#     """Village-level aggregations showing all farms"""
    
#     st.markdown("### 🏘️ Village-level Water Level Aggregations")
#     st.markdown("*Showing all farms aggregated by village*")
    
#     if 'Village' not in merged_df.columns:
#         st.error("Village information not available in the data.")
#         return
    
#     # Calculate village-level daily averages
#     village_daily = merged_df.groupby(['Village', 'Days from TPR']).agg({
#         'Water Level (mm)': 'mean',
#         'Farm ID': 'nunique'
#     }).reset_index()
    
#     village_daily.rename(columns={'Farm ID': 'Farm Count'}, inplace=True)
    
#     # Create village comparison chart
#     fig = go.Figure()
    
#     villages = sorted(village_daily['Village'].unique())
#     colors = px.colors.qualitative.Set3
    
#     for i, village in enumerate(villages):
#         village_data = village_daily[village_daily['Village'] == village]
#         village_data = village_data.sort_values('Days from TPR')
        
#         fig.add_trace(go.Scatter(
#             x=village_data['Days from TPR'],
#             y=village_data['Water Level (mm)'],
#             mode='lines+markers',
#             name=village,
#             line=dict(color=colors[i % len(colors)], width=3),
#             marker=dict(size=8),
#             hovertemplate="<b>%{text}</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>",
#             text=[village] * len(village_data)
#         ))
    
#     fig.update_layout(
#         title="Village-level Water Level Trends Comparison",
#         xaxis_title="Days from Transplanting",
#         yaxis_title="Average Water Level (mm)",
#         legend=dict(
#             orientation="v",
#             yanchor="middle",
#             y=0.5,
#             xanchor="left",
#             x=1.02
#         ),
#         height=600,
#         hovermode="x unified"
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Village summary statistics table
#     st.markdown("### 📊 Village Summary Statistics")
    
#     village_summary = merged_df.groupby('Village').agg({
#         'Water Level (mm)': ['mean', 'std', 'min', 'max', 'count'],
#         'Farm ID': 'nunique',
#         'Days from TPR': ['min', 'max']
#     }).round(2)
    
#     # Flatten column names
#     village_summary.columns = [
#         'Avg Water Level (mm)', 'Std Dev (mm)', 'Min Level (mm)', 
#         'Max Level (mm)', 'Total Readings', 'Unique Farms',
#         'Min Days from TPR', 'Max Days from TPR'
#     ]
    
#     village_summary = village_summary.reset_index()
    
#     st.dataframe(
#         village_summary.style.format({
#             'Avg Water Level (mm)': '{:.1f}',
#             'Std Dev (mm)': '{:.1f}',
#             'Min Level (mm)': '{:.1f}',
#             'Max Level (mm)': '{:.1f}'
#         }),
#         use_container_width=True
#     )
    
#     # Download village analysis
#     csv_buffer = io.StringIO()
#     village_summary.to_csv(csv_buffer, index=False)
#     st.download_button(
#         label="📥 Download Village Analysis",
#         data=csv_buffer.getvalue(),
#         file_name="village_level_analysis.csv",
#         mime="text/csv"
#     )

# def render_remote_controllers_analysis(merged_df, kharif_df):
#     """Remote Controllers: Treatment vs Control (Complied Groups)"""
    
#     st.markdown("### 🎛️ Remote Controllers Study: Treatment vs Control")
#     st.markdown("*Comparing complied groups from treatment and control*")
    
#     # Create study group classifications
#     study_data = pd.merge(
#         merged_df,
#         kharif_df[[
#             'Kharif 25 Farm ID',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'
#         ]],
#         left_on='Farm ID',
#         right_on='Kharif 25 Farm ID',
#         how='left'
#     )
    
#     # Filter for complied groups
#     treatment_complied = study_data[
#         study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'] == 1
#     ]
    
#     control_complied = study_data[
#         study_data['Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'] == 1
#     ]
    
#     if treatment_complied.empty and control_complied.empty:
#         st.warning("⚠️ No Remote Controllers study data found with compliance information.")
#         return
    
#     # Create comparison chart
#     fig = go.Figure()
    
#     if not treatment_complied.empty:
#         treatment_daily = treatment_complied.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#         treatment_daily = treatment_daily.sort_values('Days from TPR')
        
#         fig.add_trace(go.Scatter(
#             x=treatment_daily['Days from TPR'],
#             y=treatment_daily['Water Level (mm)'],
#             mode='lines+markers',
#             name='Treatment Group (A) - Complied',
#             line=dict(color='blue', width=4),
#             marker=dict(size=10),
#             hovertemplate="<b>Treatment Group (Complied)</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>"
#         ))
    
#     if not control_complied.empty:
#         control_daily = control_complied.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#         control_daily = control_daily.sort_values('Days from TPR')
        
#         fig.add_trace(go.Scatter(
#             x=control_daily['Days from TPR'],
#             y=control_daily['Water Level (mm)'],
#             mode='lines+markers',
#             name='Control Group (B) - Complied',
#             line=dict(color='red', width=4),
#             marker=dict(size=10),
#             hovertemplate="<b>Control Group (Complied)</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>"
#         ))
    
#     fig.update_layout(
#         title="Remote Controllers Study: Treatment vs Control (Complied Groups)",
#         xaxis_title="Days from Transplanting",
#         yaxis_title="Average Water Level (mm)",
#         height=500,
#         hovermode="x unified"
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Summary statistics
#     st.markdown("### 📊 Group Comparison Statistics")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if not treatment_complied.empty:
#             st.markdown("**Treatment Group (A) - Complied:**")
#             st.metric("👥 Farms", treatment_complied['Farm ID'].nunique())
#             st.metric("📊 Avg Water Level", f"{treatment_complied['Water Level (mm)'].mean():.1f} mm")
#             st.metric("📏 Std Deviation", f"{treatment_complied['Water Level (mm)'].std():.1f} mm")
    
#     with col2:
#         if not control_complied.empty:
#             st.markdown("**Control Group (B) - Complied:**")
#             st.metric("👥 Farms", control_complied['Farm ID'].nunique())
#             st.metric("📊 Avg Water Level", f"{control_complied['Water Level (mm)'].mean():.1f} mm")
#             st.metric("📏 Std Deviation", f"{control_complied['Water Level (mm)'].std():.1f} mm")

# def render_awd_groups_analysis(merged_df, kharif_df):
#     """AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)"""
    
#     st.markdown("### 💧 AWD Study: Groups A, B, C Comparisons")
#     st.markdown("*Analyzing complied and non-complied groups across all AWD study groups*")
    
#     # Create study group classifications
#     study_data = pd.merge(
#         merged_df,
#         kharif_df[[
#             'Kharif 25 Farm ID',
#             'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
#             'Kharif 25 - AWD Study - Group B -training only (Y/N)',
#             'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
#             'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
#             'Kharif 25 - AWD Study - Group C - Control (Y/N)',
#             'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
#             'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
#         ]],
#         left_on='Farm ID',
#         right_on='Kharif 25 Farm ID',
#         how='left'
#     )
    
#     # Create group filters
#     groups_data = {}
    
#     # Group A - Treatment
#     groups_data['Group A (Treatment) - Complied'] = study_data[
#         study_data['Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'] == 1
#     ]
#     groups_data['Group A (Treatment) - Non-Complied'] = study_data[
#         study_data['Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)'] == 1
#     ]
    
#     # Group B - Training
#     groups_data['Group B (Training) - Complied'] = study_data[
#         study_data['Kharif 25 - AWD Study - Group B - Complied (Y/N)'] == 1
#     ]
#     groups_data['Group B (Training) - Non-Complied'] = study_data[
#         study_data['Kharif 25 - AWD Study - Group B - Non-complied (Y/N)'] == 1
#     ]
    
#     # Group C - Control
#     groups_data['Group C (Control) - Complied'] = study_data[
#         study_data['Kharif 25 - AWD Study - Group C - Complied (Y/N)'] == 1
#     ]
#     groups_data['Group C (Control) - Non-Complied'] = study_data[
#         study_data['Kharif 25 - AWD Study - Group C - non-complied (Y/N)'] == 1
#     ]
    
#     # Filter out empty groups
#     available_groups = {k: v for k, v in groups_data.items() if not v.empty}
    
#     if not available_groups:
#         st.warning("⚠️ No AWD study data found.")
#         return
    
#     # Analysis options
#     analysis_option = st.selectbox(
#         "📊 Choose Analysis View:",
#         options=[
#             "All Groups Comparison",
#             "Complied vs Non-Complied Comparison",
#             "Group-wise Detailed Analysis"
#         ]
#     )
    
#     if analysis_option == "All Groups Comparison":
#         # Create comprehensive comparison chart
#         fig = go.Figure()
#         colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        
#         for i, (group_name, group_data) in enumerate(available_groups.items()):
#             if not group_data.empty:
#                 daily_avg = group_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#                 daily_avg = daily_avg.sort_values('Days from TPR')
                
#                 fig.add_trace(go.Scatter(
#                     x=daily_avg['Days from TPR'],
#                     y=daily_avg['Water Level (mm)'],
#                     mode='lines+markers',
#                     name=group_name,
#                     line=dict(color=colors[i % len(colors)], width=3),
#                     marker=dict(size=8)
#                 ))
        
#         fig.update_layout(
#             title="AWD Study: All Groups Comparison",
#             xaxis_title="Days from Transplanting",
#             yaxis_title="Average Water Level (mm)",
#             height=600,
#             hovermode="x unified"
#         )
        
#         st.plotly_chart(fig, use_container_width=True)
    
#     elif analysis_option == "Complied vs Non-Complied Comparison":
#         # Aggregate complied vs non-complied across all groups
#         complied_data = pd.concat([
#             groups_data['Group A (Treatment) - Complied'],
#             groups_data['Group B (Training) - Complied'],
#             groups_data['Group C (Control) - Complied']
#         ]).drop_duplicates()
        
#         non_complied_data = pd.concat([
#             groups_data['Group A (Treatment) - Non-Complied'],
#             groups_data['Group B (Training) - Non-Complied'],
#             groups_data['Group C (Control) - Non-Complied']
#         ]).drop_duplicates()
        
#         fig = go.Figure()
        
#         if not complied_data.empty:
#             complied_daily = complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#             fig.add_trace(go.Scatter(
#                 x=complied_daily['Days from TPR'],
#                 y=complied_daily['Water Level (mm)'],
#                 mode='lines+markers',
#                 name='All Complied Groups',
#                 line=dict(color='green', width=4),
#                 marker=dict(size=10)
#             ))
        
#         if not non_complied_data.empty:
#             non_complied_daily = non_complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#             fig.add_trace(go.Scatter(
#                 x=non_complied_daily['Days from TPR'],
#                 y=non_complied_daily['Water Level (mm)'],
#                 mode='lines+markers',
#                 name='All Non-Complied Groups',
#                 line=dict(color='red', width=4),
#                 marker=dict(size=10)
#             ))
        
#         fig.update_layout(
#             title="AWD Study: Complied vs Non-Complied Comparison",
#             xaxis_title="Days from Transplanting",
#             yaxis_title="Average Water Level (mm)",
#             height=500
#         )
        
#         st.plotly_chart(fig, use_container_width=True)
    
#     # Summary statistics table
#     st.markdown("### 📊 AWD Groups Summary Statistics")
    
#     summary_data = []
#     for group_name, group_data in available_groups.items():
#         if not group_data.empty:
#             summary_data.append({
#                 'Group': group_name,
#                 'Farms': group_data['Farm ID'].nunique(),
#                 'Total Readings': len(group_data),
#                 'Avg Water Level (mm)': round(group_data['Water Level (mm)'].mean(), 1),
#                 'Std Dev (mm)': round(group_data['Water Level (mm)'].std(), 1),
#                 'Min Level (mm)': round(group_data['Water Level (mm)'].min(), 1),
#                 'Max Level (mm)': round(group_data['Water Level (mm)'].max(), 1)
#             })
    
#     if summary_data:
#         summary_df = pd.DataFrame(summary_data)
#         st.dataframe(summary_df, use_container_width=True)

# def render_dsr_tpr_analysis(merged_df, kharif_df):
#     """DSR vs TPR Group Comparisons"""
    
#     st.markdown("### 🌱 DSR vs TPR Farming Methods Comparison")
#     st.markdown("*Comparing Direct Seeded Rice vs Transplanted Rice methods*")
    
#     # Create study group classifications
#     study_data = pd.merge(
#         merged_df,
#         kharif_df[[
#             'Kharif 25 Farm ID',
#             'Kharif 25 - DSR farm Study (Y/N)',
#             'Kharif 25 - TPR Group Study (Y/N)'
#         ]],
#         left_on='Farm ID',
#         right_on='Kharif 25 Farm ID',
#         how='left'
#     )
    
#     # Filter for each method
#     dsr_farms = study_data[study_data['Kharif 25 - DSR farm Study (Y/N)'] == 1]
#     tpr_farms = study_data[study_data['Kharif 25 - TPR Group Study (Y/N)'] == 1]
    
#     if dsr_farms.empty and tpr_farms.empty:
#         st.warning("⚠️ No DSR or TPR study data found.")
#         return
    
#     # Create comparison chart
#     fig = go.Figure()
    
#     if not dsr_farms.empty:
#         dsr_daily = dsr_farms.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#         dsr_daily = dsr_daily.sort_values('Days from TPR')
        
#         fig.add_trace(go.Scatter(
#             x=dsr_daily['Days from TPR'],
#             y=dsr_daily['Water Level (mm)'],
#             mode='lines+markers',
#             name='DSR (Direct Seeded Rice)',
#             line=dict(color='green', width=4),
#             marker=dict(size=10, symbol='circle'),
#             hovertemplate="<b>DSR Method</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>"
#         ))
    
#     if not tpr_farms.empty:
#         tpr_daily = tpr_farms.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
#         tpr_daily = tpr_daily.sort_values('Days from TPR')
        
#         fig.add_trace(go.Scatter(
#             x=tpr_daily['Days from TPR'],
#             y=tpr_daily['Water Level (mm)'],
#             mode='lines+markers',
#             name='TPR (Transplanted Rice)',
#             line=dict(color='blue', width=4),
#             marker=dict(size=10, symbol='diamond'),
#             hovertemplate="<b>TPR Method</b><br>" +
#                          "Days from TPR: %{x}<br>" +
#                          "Avg Water Level: %{y:.1f} mm<br>" +
#                          "<extra></extra>"
#         ))
    
#     fig.update_layout(
#         title="Farming Methods Comparison: DSR vs TPR",
#         xaxis_title="Days from Transplanting/Seeding",
#         yaxis_title="Average Water Level (mm)",
#         height=500,
#         hovermode="x unified"
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Comparative statistics
#     st.markdown("### 📊 Method Comparison Statistics")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if not dsr_farms.empty:
#             st.markdown("**DSR (Direct Seeded Rice):**")
#             st.metric("👥 Farms", dsr_farms['Farm ID'].nunique())
#             st.metric("📊 Avg Water Level", f"{dsr_farms['Water Level (mm)'].mean():.1f} mm")
#             st.metric("📏 Std Deviation", f"{dsr_farms['Water Level (mm)'].std():.1f} mm")
#             st.metric("📈 Total Readings", len(dsr_farms))
    
#     with col2:
#         if not tpr_farms.empty:
#             st.markdown("**TPR (Transplanted Rice):**")
#             st.metric("👥 Farms", tpr_farms['Farm ID'].nunique())
#             st.metric("📊 Avg Water Level", f"{tpr_farms['Water Level (mm)'].mean():.1f} mm")
#             st.metric("📏 Std Deviation", f"{tpr_farms['Water Level (mm)'].std():.1f} mm")
#             st.metric("📈 Total Readings", len(tpr_farms))

# def render_compliance_analysis(merged_df, kharif_df):
#     """Comprehensive Compliance Analysis"""
    
#     st.markdown("### ✅ Comprehensive Compliance Analysis")
#     st.markdown("*Analyzing compliance rates across all studies*")
    
#     # Create comprehensive study classifications
#     study_data = pd.merge(
#         merged_df,
#         kharif_df[[
#             'Kharif 25 Farm ID',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
#             'Kharif 25 - AWD Study - Group B -training only (Y/N)',
#             'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
#             'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
#             'Kharif 25 - AWD Study - Group C - Control (Y/N)',
#             'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
#             'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
#         ]],
#         left_on='Farm ID',
#         right_on='Kharif 25 Farm ID',
#         how='left'
#     )
    
#     # Calculate compliance rates
#     compliance_data = []
    
#     # Remote Controllers compliance
#     studies = [
#         {
#             'study': 'Remote Controllers - Treatment (A)',
#             'total_col': 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
#             'complied_col': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'
#         },
#         {
#             'study': 'Remote Controllers - Control (B)',
#             'total_col': 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
#             'complied_col': 'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'
#         },
#         {
#             'study': 'AWD - Group A (Treatment)',
#             'total_col': 'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
#             'complied_col': 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'
#         },
#         {
#             'study': 'AWD - Group B (Training)',
#             'total_col': 'Kharif 25 - AWD Study - Group B -training only (Y/N)',
#             'complied_col': 'Kharif 25 - AWD Study - Group B - Complied (Y/N)'
#         },
#         {
#             'study': 'AWD - Group C (Control)',
#             'total_col': 'Kharif 25 - AWD Study - Group C - Control (Y/N)',
#             'complied_col': 'Kharif 25 - AWD Study - Group C - Complied (Y/N)'
#         }
#     ]
    
#     for study_info in studies:
#         total_farms = len(study_data[study_data[study_info['total_col']] == 1]['Farm ID'].unique())
#         complied_farms = len(study_data[study_data[study_info['complied_col']] == 1]['Farm ID'].unique())
        
#         if total_farms > 0:
#             compliance_rate = (complied_farms / total_farms) * 100
#             compliance_data.append({
#                 'Study Group': study_info['study'],
#                 'Total Farms': total_farms,
#                 'Complied Farms': complied_farms,
#                 'Non-Complied Farms': total_farms - complied_farms,
#                 'Compliance Rate (%)': round(compliance_rate, 1)
#             })
    
#     if not compliance_data:
#         st.warning("⚠️ No compliance data found.")
#         return
    
#     # Display compliance table
#     compliance_df = pd.DataFrame(compliance_data)
#     st.dataframe(compliance_df, use_container_width=True)
    
#     # Compliance visualization
#     fig = go.Figure()
    
#     fig.add_trace(go.Bar(
#         x=compliance_df['Study Group'],
#         y=compliance_df['Compliance Rate (%)'],
#         text=compliance_df['Compliance Rate (%)'].apply(lambda x: f"{x:.1f}%"),
#         textposition='auto',
#         marker_color='lightblue',
#         name='Compliance Rate'
#     ))
    
#     fig.update_layout(
#         title="Compliance Rates Across All Studies",
#         xaxis_title="Study Groups",
#         yaxis_title="Compliance Rate (%)",
#         height=400,
#         xaxis_tickangle=-45
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Detailed compliance analysis
#     st.markdown("### 📊 Detailed Compliance Breakdown")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         # Overall compliance metrics
#         total_participants = compliance_df['Total Farms'].sum()
#         total_complied = compliance_df['Complied Farms'].sum()
#         overall_compliance = (total_complied / total_participants) * 100 if total_participants > 0 else 0
        
#         st.metric("🎯 Overall Compliance Rate", f"{overall_compliance:.1f}%")
#         st.metric("👥 Total Participating Farms", total_participants)
#         st.metric("✅ Total Complied Farms", total_complied)
    
#     with col2:
#         # Best and worst performing groups
#         if not compliance_df.empty:
#             best_group = compliance_df.loc[compliance_df['Compliance Rate (%)'].idxmax()]
#             worst_group = compliance_df.loc[compliance_df['Compliance Rate (%)'].idxmin()]
            
#             st.success(f"🏆 Best Compliance: {best_group['Study Group']} ({best_group['Compliance Rate (%)']}%)")
#             st.error(f"⚠️ Lowest Compliance: {worst_group['Study Group']} ({worst_group['Compliance Rate (%)']}%)")

# def create_comprehensive_downloads(merged_df, kharif_df, farm_daily_avg, weekly_avg):
#     """Create comprehensive download section with all data exports"""
    
#     st.markdown('<div class="section-header">💾 Comprehensive Data Downloads</div>', unsafe_allow_html=True)
    
#     st.markdown("### 📋 Available Data Exports")
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.markdown("**📊 Complete Datasets**")
        
#         # Complete merged dataset
#         csv_buffer = io.StringIO()
#         merged_df.to_csv(csv_buffer, index=False)
#         st.download_button(
#             label="📥 Complete Merged Dataset",
#             data=csv_buffer.getvalue(),
#             file_name="complete_merged_agricultural_data.csv",
#             mime="text/csv",
#             help="All water level data merged with farm information"
#         )
        
#         # Raw Kharif data
#         csv_buffer = io.StringIO()
#         kharif_df.to_csv(csv_buffer, index=False)
#         st.download_button(
#             label="📥 Raw Kharif Data",
#             data=csv_buffer.getvalue(),
#             file_name="raw_kharif_farm_data.csv",
#             mime="text/csv",
#             help="Original farm and study group data"
#         )
    
#     with col2:
#         st.markdown("**👥 Study Group Data**")
        
#         # Create study group datasets
#         study_groups = create_study_group_datasets(merged_df, kharif_df)
        
#         for group_name, group_data in study_groups.items():
#             if not group_data.empty:
#                 csv_buffer = io.StringIO()
#                 group_data.to_csv(csv_buffer, index=False)
#                 st.download_button(
#                     label=f"📥 {group_name}",
#                     data=csv_buffer.getvalue(),
#                     file_name=f"{group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}_data.csv",
#                     mime="text/csv",
#                     help=f"Data for {group_name} participants"
#                 )
    
#     with col3:
#         st.markdown("**📈 Analysis Reports**")
        
#         # Village summary
#         if 'Village' in merged_df.columns:
#             village_summary = merged_df.groupby('Village').agg({
#                 'Water Level (mm)': ['mean', 'std', 'count'],
#                 'Farm ID': 'nunique'
#             }).round(2)
#             village_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Unique Farms']
            
#             csv_buffer = io.StringIO()
#             village_summary.to_csv(csv_buffer)
#             st.download_button(
#                 label="📥 Village Summary",
#                 data=csv_buffer.getvalue(),
#                 file_name="village_summary_report.csv",
#                 mime="text/csv",
#                 help="Statistical summary by village"
#             )
        
#         # Farm summary
#         farm_summary = merged_df.groupby('Farm ID').agg({
#             'Water Level (mm)': ['mean', 'std', 'count'],
#             'Days from TPR': ['min', 'max']
#         }).round(2)
#         farm_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Min Days', 'Max Days']
        
#         csv_buffer = io.StringIO()
#         farm_summary.to_csv(csv_buffer)
#         st.download_button(
#             label="📥 Farm Summary",
#             data=csv_buffer.getvalue(),
#             file_name="farm_summary_report.csv",
#             mime="text/csv",
#             help="Statistical summary by farm"
#         )
    
#     # Create comprehensive ZIP download
#     st.markdown("### 📦 Complete Data Package")
#     st.markdown("*Download all datasets and reports in a single ZIP file*")
    
#     if st.button("🗜️ Generate Complete Data Package", help="Create ZIP file with all data"):
#         create_zip_package(merged_df, kharif_df, farm_daily_avg, weekly_avg)

# def create_study_group_datasets(merged_df, kharif_df):
#     """Create datasets for each study group"""
    
#     # Merge for study group classifications
#     study_data = pd.merge(
#         merged_df,
#         kharif_df[[
#             'Kharif 25 Farm ID',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
#             'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
#             'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
#             'Kharif 25 - AWD Study - Group B -training only (Y/N)',
#             'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
#             'Kharif 25 - AWD Study - Group C - Control (Y/N)',
#             'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
#             'Kharif 25 - TPR Group Study (Y/N)',
#             'Kharif 25 - DSR farm Study (Y/N)'
#         ]],
#         left_on='Farm ID',
#         right_on='Kharif 25 Farm ID',
#         how='left'
#     )
    
#     study_groups = {}
    
#     # Remote Controllers groups
#     rc_treatment = study_data[study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'] == 1]
#     if not rc_treatment.empty:
#         study_groups['Remote Controllers Treatment'] = rc_treatment
    
#     rc_control = study_data[study_data['Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'] == 1]
#     if not rc_control.empty:
#         study_groups['Remote Controllers Control'] = rc_control
    
#     # AWD groups
#     awd_a = study_data[study_data['Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'] == 1]
#     if not awd_a.empty:
#         study_groups['AWD Group A Treatment'] = awd_a
    
#     awd_b = study_data[study_data['Kharif 25 - AWD Study - Group B - Complied (Y/N)'] == 1]
#     if not awd_b.empty:
#         study_groups['AWD Group B Training'] = awd_b
    
#     awd_c = study_data[study_data['Kharif 25 - AWD Study - Group C - Complied (Y/N)'] == 1]
#     if not awd_c.empty:
#         study_groups['AWD Group C Control'] = awd_c
    
#     # Farming methods
#     dsr_group = study_data[study_data['Kharif 25 - DSR farm Study (Y/N)'] == 1]
#     if not dsr_group.empty:
#         study_groups['DSR Farms'] = dsr_group
    
#     tpr_group = study_data[study_data['Kharif 25 - TPR Group Study (Y/N)'] == 1]
#     if not tpr_group.empty:
#         study_groups['TPR Farms'] = tpr_group
    
#     return study_groups

# def create_zip_package(merged_df, kharif_df, farm_daily_avg, weekly_avg):
#     """Create comprehensive ZIP package with all data"""
    
#     zip_buffer = io.BytesIO()
    
#     with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        
#         # Add main datasets
#         csv_buffer = io.StringIO()
#         merged_df.to_csv(csv_buffer, index=False)
#         zip_file.writestr("01_complete_merged_data.csv", csv_buffer.getvalue())
        
#         csv_buffer = io.StringIO()
#         kharif_df.to_csv(csv_buffer, index=False)
#         zip_file.writestr("02_raw_kharif_data.csv", csv_buffer.getvalue())
        
#         # Add processed datasets
#         if not farm_daily_avg.empty:
#             csv_buffer = io.StringIO()
#             farm_daily_avg.to_csv(csv_buffer, index=False)
#             zip_file.writestr("03_farm_daily_averages.csv", csv_buffer.getvalue())
        
#         if not weekly_avg.empty:
#             csv_buffer = io.StringIO()
#             weekly_avg.to_csv(csv_buffer, index=False)
#             zip_file.writestr("04_weekly_averages.csv", csv_buffer.getvalue())
        
#         # Add study group datasets
#         study_groups = create_study_group_datasets(merged_df, kharif_df)
#         for i, (group_name, group_data) in enumerate(study_groups.items(), 5):
#             if not group_data.empty:
#                 csv_buffer = io.StringIO()
#                 group_data.to_csv(csv_buffer, index=False)
#                 filename = f"{i:02d}_{group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.csv"
#                 zip_file.writestr(filename, csv_buffer.getvalue())
        
#         # Add summary reports
#         if 'Village' in merged_df.columns:
#             village_summary = merged_df.groupby('Village').agg({
#                 'Water Level (mm)': ['mean', 'std', 'count'],
#                 'Farm ID': 'nunique'
#             }).round(2)
#             village_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Unique Farms']
            
#             csv_buffer = io.StringIO()
#             village_summary.to_csv(csv_buffer)
#             zip_file.writestr("20_village_summary.csv", csv_buffer.getvalue())
        
#         farm_summary = merged_df.groupby('Farm ID').agg({
#             'Water Level (mm)': ['mean', 'std', 'count'],
#             'Days from TPR': ['min', 'max']
#         }).round(2)
#         farm_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Min Days', 'Max Days']
        
#         csv_buffer = io.StringIO()
#         farm_summary.to_csv(csv_buffer)
#         zip_file.writestr("21_farm_summary.csv", csv_buffer.getvalue())
        
#         # Add README
#         readme_content = """
# Agricultural Data Analysis Package
# =================================

# This package contains:

# Main Datasets:
# - 01_complete_merged_data.csv: All water level data merged with farm information
# - 02_raw_kharif_data.csv: Original farm and study group data
# - 03_farm_daily_averages.csv: Daily averages per farm
# - 04_weekly_averages.csv: Weekly averages per farm

# Study Groups:
# - Remote Controllers Treatment/Control groups
# - AWD Study Groups A, B, C
# - DSR and TPR farming method groups

# Summary Reports:
# - 20_village_summary.csv: Statistics by village
# - 21_farm_summary.csv: Statistics by farm

# Generated on: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         zip_file.writestr("README.txt", readme_content)
    
#     zip_buffer.seek(0)
    
#     st.download_button(
#         label="📦 Download Complete Package (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"agricultural_data_complete_package_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
#         mime="application/zip",
#         help="Complete package with all datasets and reports"
#     )

# def main():
#     """Enhanced main function with complete dashboard functionality"""
    
#     # Main title
#     st.markdown('<div class="main-header">🌾 Enhanced Agricultural Data Analysis Dashboard</div>', unsafe_allow_html=True)
#     st.markdown("*Comprehensive analysis with advanced filtering, comparisons, and enhanced downloads*")
    
#     # Add navigation to 2024 analysis
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         st.link_button("🔗 Analyze 2024 Data", "https://v45bgthcmmrztmbstkddra.streamlit.app/", use_container_width=True)
    
#     st.markdown("---")
    
#     # Load and validate data
#     kharif_df, water_df = load_and_validate_data()
    
#     if kharif_df is not None and water_df is not None:
        
#         # Data processing with progress indicator
#         with st.spinner("🔄 Processing and cleaning data..."):
#             kharif_cleaned, water_cleaned = clean_and_process_data(kharif_df, water_df)
            
#             # Create filters
#             filters = create_advanced_filters(kharif_cleaned, water_cleaned)
            
#             # Apply filters
#             filtered_kharif, filtered_water = apply_comprehensive_filters(kharif_cleaned, water_cleaned, filters)
            
#             # Create merged dataset
#             merged_df, farm_daily_avg, weekly_avg = create_merged_dataset(filtered_kharif, filtered_water)
        
#         # Display data overview in sidebar
#         with st.sidebar:
#             st.markdown('<div class="section-header">📊 Data Overview</div>', unsafe_allow_html=True)
            
#             st.markdown(f"""
#             **📈 Current Dataset:**
#             - **Merged Records:** {len(merged_df):,}
#             - **Unique Farms:** {merged_df['Farm ID'].nunique() if not merged_df.empty else 0:,}
#             - **Villages:** {merged_df['Village'].nunique() if 'Village' in merged_df.columns and not merged_df.empty else 0:,}
#             - **Date Range:** {merged_df['Date'].min().strftime('%Y-%m-%d') if not merged_df.empty else 'N/A'} to {merged_df['Date'].max().strftime('%Y-%m-%d') if not merged_df.empty else 'N/A'}
#             """)
            
#             if not merged_df.empty:
#                 avg_water_level = merged_df['Water Level (mm)'].mean()
#                 st.markdown(f"- **Avg Water Level:** {avg_water_level:.1f} mm")
            
#             st.markdown("---")
#             st.markdown("**📋 Original Data:**")
#             st.markdown(f"- **Kharif Records:** {len(kharif_df):,}")
#             st.markdown(f"- **Water Records:** {len(water_df):,}")
        
#         if merged_df.empty:
#             st.warning("⚠️ No data available after applying filters. Please adjust your filter settings.")
            
#             with st.expander("🔧 Troubleshooting Tips"):
#                 st.markdown("""
#                 **Common Issues:**
#                 - **Date Range:** Ensure selected dates overlap with your data
#                 - **Village Names:** Check for typos or variations in village names
#                 - **Study Groups:** Verify that selected groups have data
#                 - **Farm IDs:** Ensure farm IDs match between datasets
                
#                 **Try:**
#                 - Reset filters to "All" options
#                 - Check the original data structure
#                 - Expand date range selection
#                 """)
#         else:
#             st.success(f"✅ Successfully processed {len(merged_df):,} records from {merged_df['Farm ID'].nunique()} farms!")
            
#             # Create main tabs
#             tab1, tab2, tab3 = st.tabs([
#                 "🏡 Individual Farm Analysis",
#                 "👥 Comparative Analysis",
#                 "💾 Data Downloads"
#             ])
            
#             with tab1:
#                 render_individual_farm_analysis(merged_df, farm_daily_avg, weekly_avg)
            
#             with tab2:
#                 render_comparative_analysis(merged_df, filtered_kharif)
            
#             with tab3:
#                 create_comprehensive_downloads(merged_df, filtered_kharif, farm_daily_avg, weekly_avg)
    
#     else:
#         # Data upload instructions
#         st.info("📁 Please upload both Excel files to begin analysis.")
        
#         with st.expander("ℹ️ Expected Data Structure & Features", expanded=True):
#             st.markdown("""
#             ### 📋 Required Files:
            
#             **1. Kharif 25 Excel File:**
#             - `Kharif 25 Farm ID` - Unique farm identifier
#             - `Kharif 25 Village` - Village name
#             - `Kharif 25 Paddy transplanting date (TPR)` - Transplanting date
#             - Study group columns (Remote Controllers, AWD, TPR, DSR)
#             - PVC Pipe codes (1-5)
#             - Compliance indicators (Y/N)
            
#             **2. Water Level Measurement Excel File:**
#             - `Date` - Measurement date
#             - `Farm ID` - Farm identifier (must match Kharif file)
#             - `Pipe code ID of the farm` - Pipe identifier
#             - `Measure water level inside the PVC pipe - millimeter mm` - Water level reading
#             - `Village name` - Village name
            
#             ### ✨ Enhanced Features:
            
#             **🔍 Advanced Filters:**
#             - 📅 Date range selection with validation
#             - 🏘️ Village-specific filtering with typo handling
#             - 🔬 Study group filtering (RC, AWD, TPR, DSR)
#             - ✅ Compliance status filtering
#             - 🔧 Data quality filters (minimum readings, outlier removal)
            
#             **📊 Complete Analysis:**
#             - **Graph 1:** Daily water levels per pipe + farm average (markers only)
#             - **Graph 2:** Weekly water level trends (markers + farm average line)
#             - **Table 3:** Water level data with Days from TPR as Column A
#             - **Comparative Charts:** All required study group comparisons
            
#             **👥 Study Group Comparisons:**
#             - Remote Controllers: Treatment vs Control (complied groups)
#             - AWD Study: Groups A, B, C (complied and non-complied)
#             - DSR vs TPR group comparisons
#             - Village-level aggregations
#             - Comprehensive compliance analysis
            
#             **💾 Enhanced Downloads:**
#             - Individual farm reports (detailed + summary)
#             - Study group datasets (separate CSV files)
#             - Village and farm summary reports
#             - Complete data packages (ZIP format)
            
#             **🔧 Data Quality Features:**
#             - Fuzzy matching for village names (handles typos)
#             - Case insensitive comparisons
#             - Data normalization and cleaning
#             - Outlier detection and removal
#             - Missing data handling
            
#             **📈 Advanced Visualizations:**
#             - Interactive charts with hover information
#             - Color-coded study groups
#             - Responsive design for all screen sizes
#             - Export-ready chart formats
#             """)

# if __name__ == "__main__":
#     main()

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import io
import re
import zipfile
import warnings
warnings.filterwarnings('ignore')

# Configure page
st.set_page_config(
    page_title="Enhanced Agricultural Data Analysis Dashboard",
    page_icon="🌾",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #1976D2;
        border-bottom: 2px solid #1976D2;
        padding-bottom: 0.5rem;
        margin: 1.5rem 0 1rem 0;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .filter-section {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .debug-info {
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 0.25rem;
        border-left: 4px solid #17a2b8;
        margin: 0.5rem 0;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

def normalize_text(text):
    """Normalize text for consistent comparison"""
    if pd.isna(text) or text is None:
        return ""
    text = str(text).strip().lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def fuzzy_match_villages(village_list, threshold=85):
    """Group similar village names using simple similarity"""
    if not village_list:
        return []
    
    normalized_villages = {}
    for village in village_list:
        if pd.isna(village):
            continue
        
        norm_village = normalize_text(village)
        if not norm_village:
            continue
            
        # Check for exact matches first
        found_match = False
        for existing_norm, original in normalized_villages.items():
            if norm_village == existing_norm:
                found_match = True
                break
            # Simple similarity check
            if len(norm_village) > 3 and len(existing_norm) > 3:
                if norm_village in existing_norm or existing_norm in norm_village:
                    found_match = True
                    break
        
        if not found_match:
            normalized_villages[norm_village] = str(village).strip()
    
    return sorted(list(normalized_villages.values()))

def convert_binary_column(series):
    """Convert Y/N, Yes/No, 1/0 to consistent 1/0 format"""
    if series.dtype == 'object':
        # Handle string values
        return series.apply(lambda x: 1 if str(x).upper().strip() in ['Y', 'YES', '1', 'TRUE'] else 0)
    else:
        # Handle numeric values
        return series.apply(lambda x: 1 if pd.notna(x) and (x == 1 or x == '1') else 0)

def load_and_validate_data():
    """Load and validate uploaded Excel files"""
    st.markdown('<div class="section-header">📁 Data Upload Section</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Upload Kharif 25 Excel File**")
        kharif_file = st.file_uploader(
            "Choose Kharif file", 
            type=['xlsx', 'xls'],
            help="Upload the main farm data file with study group information"
        )
        if kharif_file:
            st.success("✅ Kharif file uploaded successfully")
    
    with col2:
        st.markdown("**Upload Water Level Excel File**")
        water_file = st.file_uploader(
            "Choose Water Level file", 
            type=['xlsx', 'xls'],
            help="Upload the water level measurement data file"
        )
        if water_file:
            st.success("✅ Water level file uploaded successfully")
    
    if kharif_file is not None and water_file is not None:
        try:
            with st.spinner("📊 Loading and validating data..."):
                # Load data
                kharif_df = pd.read_excel(kharif_file)
                water_df = pd.read_excel(water_file)
                
                # Validate required columns
                required_kharif_cols = [
                    'Kharif 25 Farm ID',
                    'Kharif 25 Village',
                    'Kharif 25 Paddy transplanting date (TPR)'
                ]
                
                required_water_cols = [
                    'Date',
                    'Farm ID',
                    'Pipe code ID of the farm',
                    'Measure water level inside the PVC pipe - millimeter mm'
                ]
                
                missing_kharif = [col for col in required_kharif_cols if col not in kharif_df.columns]
                missing_water = [col for col in required_water_cols if col not in water_df.columns]
                
                if missing_kharif:
                    st.error(f"❌ Missing columns in Kharif file: {missing_kharif}")
                    return None, None
                
                if missing_water:
                    st.error(f"❌ Missing columns in Water file: {missing_water}")
                    return None, None
                
                st.success("✅ Data validation completed successfully!")
                return kharif_df, water_df
                
        except Exception as e:
            st.error(f"❌ Error loading files: {str(e)}")
            return None, None
    
    return None, None

def clean_and_process_data(kharif_df, water_df):
    """Enhanced data cleaning and processing"""
    
    kharif_cleaned = kharif_df.copy()
    water_cleaned = water_df.copy()
    
    # Clean and normalize text columns
    if 'Kharif 25 Village' in kharif_cleaned.columns:
        kharif_cleaned['Village_Normalized'] = kharif_cleaned['Kharif 25 Village'].apply(lambda x: normalize_text(x) if pd.notna(x) else "")
        kharif_cleaned['Kharif 25 Village'] = kharif_cleaned['Kharif 25 Village'].astype(str).str.strip()
    
    if 'Village name' in water_cleaned.columns:
        water_cleaned['Village_Normalized'] = water_cleaned['Village name'].apply(lambda x: normalize_text(x) if pd.notna(x) else "")
        water_cleaned['Village name'] = water_cleaned['Village name'].astype(str).str.strip()
    
    # Clean Farm IDs
    if 'Farm ID' in water_cleaned.columns:
        water_cleaned['Farm ID'] = water_cleaned['Farm ID'].astype(str).str.strip().str.upper()
    
    if 'Kharif 25 Farm ID' in kharif_cleaned.columns:
        kharif_cleaned['Kharif 25 Farm ID'] = kharif_cleaned['Kharif 25 Farm ID'].astype(str).str.strip().str.upper()
    
    # Handle dates properly
    if 'Date' in water_cleaned.columns:
        water_cleaned['Date'] = pd.to_datetime(water_cleaned['Date'], errors='coerce')
        water_cleaned = water_cleaned.dropna(subset=['Date'])
    
    if 'Kharif 25 Paddy transplanting date (TPR)' in kharif_cleaned.columns:
        kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'] = pd.to_datetime(
            kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'], errors='coerce'
        )
        # Fill missing TPR dates with June 1, 2025
        kharif_cleaned['Kharif 25 Paddy transplanting date (TPR)'].fillna(
            pd.Timestamp('2025-06-01'), inplace=True
        )
    
    # Clean water level measurements
    if 'Measure water level inside the PVC pipe - millimeter mm' in water_cleaned.columns:
        water_cleaned['Water_Level_Numeric'] = pd.to_numeric(
            water_cleaned['Measure water level inside the PVC pipe - millimeter mm'], 
            errors='coerce'
        )
        water_cleaned = water_cleaned.dropna(subset=['Water_Level_Numeric'])
    
    # Handle binary columns (Y/N to 1/0) - IMPROVED LOGIC
    binary_columns = [col for col in kharif_cleaned.columns if '(Y/N)' in col]
    
    if binary_columns:
        st.info(f"🔧 Processing {len(binary_columns)} binary columns for study groups...")
        
    for col in binary_columns:
        if col in kharif_cleaned.columns:
            original_values = kharif_cleaned[col].value_counts()
            kharif_cleaned[col] = convert_binary_column(kharif_cleaned[col])
            
            # Debug info for binary conversion
            converted_count = kharif_cleaned[col].sum()
            if converted_count > 0:
                st.sidebar.success(f"✅ {col.split(' - ')[-1]}: {converted_count} farms")
    
    return kharif_cleaned, water_cleaned

def get_available_study_groups(kharif_df):
    """Get available study groups and their counts"""
    study_groups = {}
    
    # Remote Controllers Study
    rc_cols = {
        'Treatment Group (A)': 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
        'Treatment Complied (A)': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
        'Treatment Non-Complied (A)': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
        'Control Group (B)': 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
        'Control Complied (B)': 'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
        'Control Non-Complied (B)': 'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)'
    }
    
    for group_name, col_name in rc_cols.items():
        if col_name in kharif_df.columns:
            count = kharif_df[col_name].sum() if kharif_df[col_name].dtype in ['int64', 'float64'] else 0
            if count > 0:
                study_groups[f"RC - {group_name}"] = {'column': col_name, 'count': count}
    
    # AWD Study
    awd_cols = {
        'Group A Treatment': 'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
        'Group A Complied': 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
        'Group A Non-Complied': 'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
        'Group B Training': 'Kharif 25 - AWD Study - Group B -training only (Y/N)',
        'Group B Complied': 'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
        'Group B Non-Complied': 'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
        'Group C Control': 'Kharif 25 - AWD Study - Group C - Control (Y/N)',
        'Group C Complied': 'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
        'Group C Non-Complied': 'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
    }
    
    for group_name, col_name in awd_cols.items():
        if col_name in kharif_df.columns:
            count = kharif_df[col_name].sum() if kharif_df[col_name].dtype in ['int64', 'float64'] else 0
            if count > 0:
                study_groups[f"AWD - {group_name}"] = {'column': col_name, 'count': count}
    
    # Farming Methods
    farming_cols = {
        'TPR Group': 'Kharif 25 - TPR Group Study (Y/N)',
        'DSR Group': 'Kharif 25 - DSR farm Study (Y/N)'
    }
    
    for group_name, col_name in farming_cols.items():
        if col_name in kharif_df.columns:
            count = kharif_df[col_name].sum() if kharif_df[col_name].dtype in ['int64', 'float64'] else 0
            if count > 0:
                study_groups[group_name] = {'column': col_name, 'count': count}
    
    return study_groups

def create_advanced_filters(kharif_df, water_df):
    """Create comprehensive filtering system with improved study group detection"""
    
    st.sidebar.markdown('<div class="section-header">🔍 Advanced Filters</div>', unsafe_allow_html=True)
    
    filters = {}
    
    # Date Range Filter
    with st.sidebar.expander("📅 Date Range Filter", expanded=True):
        if 'Date' in water_df.columns and not water_df['Date'].isna().all():
            min_date = water_df['Date'].min().date()
            max_date = water_df['Date'].max().date()
            
            date_range = st.date_input(
                "Select date range:",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date
            )
            
            if len(date_range) == 2:
                filters['date_range'] = date_range
                st.info(f"📊 Selected: {date_range[0]} to {date_range[1]}")
    
    # Village Filter
    with st.sidebar.expander("🏘️ Village Filter", expanded=True):
        villages = []
        if 'Kharif 25 Village' in kharif_df.columns:
            villages.extend(kharif_df['Kharif 25 Village'].dropna().unique())
        if 'Village name' in water_df.columns:
            villages.extend(water_df['Village name'].dropna().unique())
        
        unique_villages = fuzzy_match_villages(list(set(villages)))
        
        selected_villages = st.multiselect(
            "Select villages:",
            options=unique_villages,
            default=[],
            help="Select specific villages to analyze"
        )
        filters['villages'] = selected_villages
        
        if selected_villages:
            st.info(f"📍 Selected {len(selected_villages)} village(s)")
    
    # Study Group Filters - IMPROVED
    with st.sidebar.expander("🔬 Study Group Filters", expanded=True):
        
        # Get available study groups
        available_groups = get_available_study_groups(kharif_df)
        
        if available_groups:
            st.markdown("**Available Study Groups:**")
            
            # Show available groups with counts
            for group_name, group_info in available_groups.items():
                st.markdown(f"• {group_name}: {group_info['count']} farms")
            
            st.markdown("---")
            
            # Remote Controllers Study
            st.markdown("**Remote Controllers Study:**")
            rc_options = ["All"] + [name for name in available_groups.keys() if name.startswith("RC -")]
            rc_filter = st.selectbox(
                "RC Group:",
                options=rc_options,
                help="Filter by Remote Controllers study groups"
            )
            filters['remote_controllers'] = rc_filter
            
            # AWD Study
            st.markdown("**AWD Study:**")
            awd_options = ["All"] + [name for name in available_groups.keys() if name.startswith("AWD -")]
            awd_filter = st.selectbox(
                "AWD Group:",
                options=awd_options,
                help="Filter by AWD study groups"
            )
            filters['awd_study'] = awd_filter
            
            # Farming Method
            st.markdown("**Farming Method:**")
            farming_options = ["All"] + [name for name in available_groups.keys() if name in ["TPR Group", "DSR Group"]]
            farming_method = st.selectbox(
                "Method:",
                options=farming_options,
                help="Filter by farming method"
            )
            filters['farming_method'] = farming_method
            
            # Store available groups for filter application
            filters['available_groups'] = available_groups
            
        else:
            st.warning("⚠️ No study groups detected. Check if binary columns contain valid data.")
    
    # Data Quality Filters
    with st.sidebar.expander("🔧 Data Quality", expanded=False):
        
        min_readings = st.number_input(
            "Min readings per farm:",
            min_value=1,
            max_value=100,
            value=1,
            help="Minimum number of water level readings per farm"
        )
        filters['min_readings'] = min_readings
        
        outlier_filter = st.checkbox(
            "Remove outliers",
            value=False,
            help="Remove statistical outliers from water level data"
        )
        filters['remove_outliers'] = outlier_filter
    
    return filters

def apply_comprehensive_filters(kharif_df, water_df, filters):
    """Apply all selected filters to the datasets - IMPROVED"""
    
    filtered_kharif = kharif_df.copy()
    filtered_water = water_df.copy()
    
    # Apply date filter
    if 'date_range' in filters and len(filters['date_range']) == 2:
        start_date, end_date = filters['date_range']
        filtered_water = filtered_water[
            (filtered_water['Date'] >= pd.Timestamp(start_date)) &
            (filtered_water['Date'] <= pd.Timestamp(end_date))
        ]
    
    # Apply village filter
    if filters['villages']:
        # Normalize selected villages for comparison
        normalized_selected = [normalize_text(v) for v in filters['villages']]
        
        if 'Village_Normalized' in filtered_kharif.columns:
            filtered_kharif = filtered_kharif[
                filtered_kharif['Village_Normalized'].isin(normalized_selected)
            ]
        
        if 'Village_Normalized' in filtered_water.columns:
            filtered_water = filtered_water[
                filtered_water['Village_Normalized'].isin(normalized_selected)
            ]
    
    # Apply study group filters - IMPROVED LOGIC
    available_groups = filters.get('available_groups', {})
    
    # Remote Controllers filter
    if filters.get('remote_controllers', 'All') != "All":
        selected_group = filters['remote_controllers']
        if selected_group in available_groups:
            column_name = available_groups[selected_group]['column']
            mask = filtered_kharif[column_name] == 1
            filtered_kharif = filtered_kharif[mask]
            
            # Debug info
            st.sidebar.success(f"✅ Applied RC filter: {mask.sum()} farms selected")
    
    # AWD filter
    if filters.get('awd_study', 'All') != "All":
        selected_group = filters['awd_study']
        if selected_group in available_groups:
            column_name = available_groups[selected_group]['column']
            mask = filtered_kharif[column_name] == 1
            filtered_kharif = filtered_kharif[mask]
            
            # Debug info
            st.sidebar.success(f"✅ Applied AWD filter: {mask.sum()} farms selected")
    
    # Farming method filter
    if filters.get('farming_method', 'All') != "All":
        selected_group = filters['farming_method']
        if selected_group in available_groups:
            column_name = available_groups[selected_group]['column']
            mask = filtered_kharif[column_name] == 1
            filtered_kharif = filtered_kharif[mask]
            
            # Debug info
            st.sidebar.success(f"✅ Applied farming method filter: {mask.sum()} farms selected")
    
    # Apply minimum readings filter
    if 'min_readings' in filters and filters['min_readings'] > 1:
        farm_counts = filtered_water['Farm ID'].value_counts()
        valid_farms = farm_counts[farm_counts >= filters['min_readings']].index
        filtered_water = filtered_water[filtered_water['Farm ID'].isin(valid_farms)]
    
    # Apply outlier removal
    if filters.get('remove_outliers', False) and 'Water_Level_Numeric' in filtered_water.columns:
        Q1 = filtered_water['Water_Level_Numeric'].quantile(0.25)
        Q3 = filtered_water['Water_Level_Numeric'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        filtered_water = filtered_water[
            (filtered_water['Water_Level_Numeric'] >= lower_bound) &
            (filtered_water['Water_Level_Numeric'] <= upper_bound)
        ]
    
    return filtered_kharif, filtered_water

def create_merged_dataset(kharif_df, water_df):
    """Create comprehensive merged dataset with all calculations"""
    
    # Select relevant columns for merging
    kharif_cols = [
        "Kharif 25 Farm ID",
        "Kharif 25 Village",
        "Kharif 25 Paddy transplanting date (TPR)"
    ]
    
    # Add pipe code columns if they exist
    for i in range(1, 6):
        pipe_col = f"Kharif 25 PVC Pipe code - {i}"
        if pipe_col in kharif_df.columns:
            kharif_cols.append(pipe_col)
    
    kharif_subset = kharif_df[kharif_cols].copy()
    
    # Select water level columns
    water_cols = [
        "Date",
        "Farm ID",
        "Village name",
        "Pipe code ID of the farm"
    ]
    
    # Handle different possible column names for water level
    water_level_col = None
    possible_water_cols = [
        "Measure water level inside the PVC pipe - millimeter mm",
        "Water_Level_Numeric",
        "Water Level (mm)"
    ]
    
    for col in possible_water_cols:
        if col in water_df.columns:
            water_level_col = col
            break
    
    if water_level_col:
        water_cols.append(water_level_col)
    
    water_subset = water_df[water_cols].copy()
    
    # Merge datasets
    merged_df = pd.merge(
        water_subset,
        kharif_subset,
        how="inner",
        left_on="Farm ID",
        right_on="Kharif 25 Farm ID"
    )
    
    # Rename columns for clarity
    column_renames = {
        water_level_col: "Water Level (mm)",
        "Kharif 25 Paddy transplanting date (TPR)": "TPR Date",
        "Kharif 25 Village": "Village"
    }
    
    merged_df.rename(columns=column_renames, inplace=True)
    
    # Calculate days and weeks from TPR
    if 'TPR Date' in merged_df.columns and 'Date' in merged_df.columns:
        merged_df["Days from TPR"] = (merged_df["Date"] - merged_df["TPR Date"]).dt.days
        merged_df["Week from TPR"] = (merged_df["Days from TPR"] / 7).astype(int)
    
    # Calculate farm-level daily averages
    if 'Water Level (mm)' in merged_df.columns:
        farm_daily_avg = merged_df.groupby(['Farm ID', 'Date']).agg({
            'Water Level (mm)': 'mean',
            'TPR Date': 'first',
            'Village': 'first'
        }).reset_index()
        
        farm_daily_avg["Days from TPR"] = (farm_daily_avg["Date"] - farm_daily_avg["TPR Date"]).dt.days
        farm_daily_avg["Week from TPR"] = (farm_daily_avg["Days from TPR"] / 7).astype(int)
        
        # Calculate weekly averages
        weekly_avg = merged_df.groupby(['Farm ID', 'Week from TPR']).agg({
            'Water Level (mm)': 'mean',
            'Village': 'first'
        }).reset_index()
        
        return merged_df, farm_daily_avg, weekly_avg
    
    return merged_df, pd.DataFrame(), pd.DataFrame()

def render_individual_farm_analysis(merged_df, farm_daily_avg, weekly_avg):
    """Complete individual farm analysis with all required graphs and tables"""
    
    st.markdown('<div class="section-header">🏡 Individual Farm Analysis</div>', unsafe_allow_html=True)
    
    if merged_df.empty:
        st.warning("⚠️ No data available for individual farm analysis. Please check your filters.")
        return
    
    # Farm selection with search
    farm_ids = sorted(merged_df["Farm ID"].dropna().unique())
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_farm = st.selectbox(
            "🔍 Select Farm ID:",
            options=farm_ids,
            help="Choose a farm to analyze in detail"
        )
    
    with col2:
        if selected_farm:
            farm_info = merged_df[merged_df["Farm ID"] == selected_farm].iloc[0]
            village = farm_info.get('Village', 'Unknown')
            st.info(f"📍 Village: {village}")
    
    if not selected_farm:
        st.warning("Please select a farm ID to proceed.")
        return
    
    # Filter data for selected farm
    farm_data = merged_df[merged_df["Farm ID"] == selected_farm].copy()
    farm_daily_data = farm_daily_avg[farm_daily_avg["Farm ID"] == selected_farm].copy()
    farm_weekly_data = weekly_avg[weekly_avg["Farm ID"] == selected_farm].copy()
    
    if farm_data.empty:
        st.warning(f"⚠️ No data found for Farm ID: {selected_farm}")
        return
    
    # Get available pipes
    available_pipes = sorted(farm_data["Pipe code ID of the farm"].dropna().unique())
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_pipes = st.multiselect(
            "🔧 Select Pipes to Analyze:",
            options=available_pipes,
            default=available_pipes[:3] if len(available_pipes) > 3 else available_pipes,
            help="Choose which pipes to include in the analysis"
        )
    
    with col2:
        st.metric("📊 Total Readings", len(farm_data))
        st.metric("🔧 Available Pipes", len(available_pipes))
    
    if not selected_pipes:
        st.warning("⚠️ Please select at least one pipe to analyze.")
        return
    
    # Filter for selected pipes
    filtered_farm_data = farm_data[farm_data["Pipe code ID of the farm"].isin(selected_pipes)].copy()
    
    # **GRAPH 1: Daily Water Levels per Pipe + Farm Average**
    st.markdown("### 📊 Graph 1: Daily Water Levels per Pipe + Farm Average")
    
    fig1 = go.Figure()
    
    # Color palette for pipes
    colors = px.colors.qualitative.Set3
    
    # Add each pipe as markers only
    for i, pipe in enumerate(selected_pipes):
        pipe_data = filtered_farm_data[filtered_farm_data["Pipe code ID of the farm"] == pipe].copy()
        pipe_data = pipe_data.sort_values("Days from TPR")
        
        fig1.add_trace(go.Scatter(
            x=pipe_data["Days from TPR"],
            y=pipe_data["Water Level (mm)"],
            mode='markers',
            name=f"Pipe {pipe}",
            marker=dict(
                size=8,
                color=colors[i % len(colors)],
                opacity=0.7
            ),
            hovertemplate="<b>Pipe %{text}</b><br>" +
                         "Days from TPR: %{x}<br>" +
                         "Water Level: %{y:.1f} mm<br>" +
                         "<extra></extra>",
            text=[pipe] * len(pipe_data)
        ))
    
    # Add farm average as line + markers
    if not farm_daily_data.empty:
        farm_daily_sorted = farm_daily_data.sort_values("Days from TPR")
        fig1.add_trace(go.Scatter(
            x=farm_daily_sorted["Days from TPR"],
            y=farm_daily_sorted["Water Level (mm)"],
            mode='lines+markers',
            name="Farm Average",
            line=dict(width=4, color='black'),
            marker=dict(symbol='diamond', size=12, color='black'),
            hovertemplate="<b>Farm Average</b><br>" +
                         "Days from TPR: %{x}<br>" +
                         "Water Level: %{y:.1f} mm<br>" +
                         "<extra></extra>"
        ))
    
    fig1.update_layout(
        title=f"Daily Water Levels - Farm {selected_farm}",
        xaxis_title="Days from Transplanting",
        yaxis_title="PVC Water Level (mm)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode="x unified",
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # **GRAPH 2: Weekly Water Level Trends**
    st.markdown("### 📈 Graph 2: Weekly Water Level Trends per Pipe + Farm Average")
    
    fig2 = go.Figure()
    
    # Weekly averages per pipe (markers only)
    for i, pipe in enumerate(selected_pipes):
        pipe_data = filtered_farm_data[filtered_farm_data["Pipe code ID of the farm"] == pipe]
        pipe_weekly = pipe_data.groupby("Week from TPR")["Water Level (mm)"].mean().reset_index()
        pipe_weekly = pipe_weekly.sort_values("Week from TPR")
        
        fig2.add_trace(go.Scatter(
            x=pipe_weekly["Week from TPR"],
            y=pipe_weekly["Water Level (mm)"],
            mode='markers',
            name=f"Pipe {pipe}",
            marker=dict(
                size=10,
                color=colors[i % len(colors)],
                opacity=0.7
            ),
            hovertemplate="<b>Pipe %{text}</b><br>" +
                         "Week from TPR: %{x}<br>" +
                         "Avg Water Level: %{y:.1f} mm<br>" +
                         "<extra></extra>",
            text=[pipe] * len(pipe_weekly)
        ))
    
    # Farm weekly average (line + markers)
    if not farm_weekly_data.empty:
        farm_weekly_sorted = farm_weekly_data.sort_values("Week from TPR")
        fig2.add_trace(go.Scatter(
            x=farm_weekly_sorted["Week from TPR"],
            y=farm_weekly_sorted["Water Level (mm)"],
            mode='lines+markers',
            name="Farm Weekly Average",
            line=dict(width=4, color='black'),
            marker=dict(symbol='diamond', size=12, color='black'),
            hovertemplate="<b>Farm Weekly Average</b><br>" +
                         "Week from TPR: %{x}<br>" +
                         "Avg Water Level: %{y:.1f} mm<br>" +
                         "<extra></extra>"
        ))
    
    fig2.update_layout(
        title=f"Weekly Water Level Trends - Farm {selected_farm}",
        xaxis_title="Weeks from Transplanting",
        yaxis_title="PVC Water Level (mm)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode="x unified",
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # **TABLE 3: Water Level Data (All Pipes) - As Required**
    st.markdown("### 📋 Table 3: Water Level Data (All Pipes)")
    st.markdown("*Individual pipe readings with timestamps and farm averages*")
    
    # Create comprehensive table with Days from TPR as Column A
    table_data = filtered_farm_data.pivot_table(
        index="Days from TPR",
        columns="Pipe code ID of the farm",
        values="Water Level (mm)",
        aggfunc='mean'
    ).reset_index()
    
    # Add farm average column
    if not farm_daily_data.empty:
        farm_avg_for_table = farm_daily_data.set_index("Days from TPR")["Water Level (mm)"]
        table_data = table_data.set_index("Days from TPR")
        table_data["Farm Average"] = farm_avg_for_table
        table_data = table_data.reset_index()
    
    # Add date column for timestamps
    date_mapping = filtered_farm_data.groupby("Days from TPR")["Date"].first().reset_index()
    table_data = pd.merge(table_data, date_mapping, on="Days from TPR", how="left")
    
    # Reorder columns: Days from TPR (Column A), Date, Pipes, Farm Average
    pipe_cols = [col for col in table_data.columns if col not in ["Days from TPR", "Date", "Farm Average"]]
    column_order = ["Days from TPR", "Date"] + sorted(pipe_cols) + (["Farm Average"] if "Farm Average" in table_data.columns else [])
    table_data = table_data[column_order]
    
    # Format the table
    st.dataframe(
        table_data.style.format({
            col: "{:.1f}" for col in table_data.columns if col not in ["Days from TPR", "Date"]
        }).set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]},
            {'selector': 'td', 'props': [('text-align', 'center')]}
        ]),
        use_container_width=True,
        height=400
    )
    
    # Summary statistics
    st.markdown("### 📊 Farm Summary Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_level = filtered_farm_data["Water Level (mm)"].mean()
        st.metric("🌊 Average Water Level", f"{avg_level:.1f} mm")
    
    with col2:
        std_level = filtered_farm_data["Water Level (mm)"].std()
        st.metric("📏 Standard Deviation", f"{std_level:.1f} mm")
    
    with col3:
        min_level = filtered_farm_data["Water Level (mm)"].min()
        st.metric("⬇️ Minimum Level", f"{min_level:.1f} mm")
    
    with col4:
        max_level = filtered_farm_data["Water Level (mm)"].max()
        st.metric("⬆️ Maximum Level", f"{max_level:.1f} mm")
    
    # Download section for individual farm
    st.markdown("### 💾 Download Individual Farm Data")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Download detailed data
        csv_buffer = io.StringIO()
        filtered_farm_data.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Download Detailed Data",
            data=csv_buffer.getvalue(),
            file_name=f"farm_{selected_farm}_detailed_data.csv",
            mime="text/csv",
            help="All individual readings for this farm"
        )
    
    with col2:
        # Download summary table
        csv_buffer = io.StringIO()
        table_data.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Download Summary Table",
            data=csv_buffer.getvalue(),
            file_name=f"farm_{selected_farm}_summary_table.csv",
            mime="text/csv",
            help="Table 3 data as shown above"
        )
    
    with col3:
        # Download daily averages
        if not farm_daily_data.empty:
            csv_buffer = io.StringIO()
            farm_daily_data.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download Daily Averages",
                data=csv_buffer.getvalue(),
                file_name=f"farm_{selected_farm}_daily_averages.csv",
                mime="text/csv",
                help="Farm daily average calculations"
            )

def render_comparative_analysis(merged_df, kharif_df):
    """Comprehensive comparative analysis with all study group comparisons"""
    
    st.markdown('<div class="section-header">👥 Comparative Analysis</div>', unsafe_allow_html=True)
    
    if merged_df.empty:
        st.warning("⚠️ No data available for comparative analysis. Please check your filters.")
        return
    
    # Analysis type selection
    analysis_type = st.selectbox(
        "📊 Select Analysis Type:",
        options=[
            "Village-level Aggregations",
            "Remote Controllers: Treatment vs Control (Complied Groups)",
            "AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)",
            "DSR vs TPR Group Comparisons",
            "Comprehensive Compliance Analysis",
            "Custom Village/Farm Selection"
        ],
        help="Choose the type of comparative analysis to perform"
    )
    
    if analysis_type == "Village-level Aggregations":
        render_village_level_analysis(merged_df)
    elif analysis_type == "Remote Controllers: Treatment vs Control (Complied Groups)":
        render_remote_controllers_analysis(merged_df, kharif_df)
    elif analysis_type == "AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied)":
        render_awd_groups_analysis(merged_df, kharif_df)
    elif analysis_type == "DSR vs TPR Group Comparisons":
        render_dsr_tpr_analysis(merged_df, kharif_df)
    elif analysis_type == "Comprehensive Compliance Analysis":
        render_compliance_analysis(merged_df, kharif_df)
    elif analysis_type == "Custom Village/Farm Selection":
        render_custom_selection_analysis(merged_df, kharif_df)

def render_village_level_analysis(merged_df):
    """Village-level aggregations showing all farms with village selection"""
    
    st.markdown("### 🏘️ Village-level Water Level Aggregations")
    st.markdown("*Showing all farms aggregated by village*")
    
    if 'Village' not in merged_df.columns:
        st.error("Village information not available in the data.")
        return
    
    # Village selection options
    available_villages = sorted(merged_df['Village'].unique())
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_villages = st.multiselect(
            "🏘️ Select Villages to Compare:",
            options=available_villages,
            default=available_villages,
            help="Choose specific villages for comparison"
        )
    
    with col2:
        if selected_villages:
            st.info(f"📊 Analyzing {len(selected_villages)} village(s)")
            total_farms = merged_df[merged_df['Village'].isin(selected_villages)]['Farm ID'].nunique()
            st.metric("🏡 Total Farms", total_farms)
    
    if not selected_villages:
        st.warning("⚠️ Please select at least one village to analyze.")
        return
    
    # Filter data for selected villages
    filtered_df = merged_df[merged_df['Village'].isin(selected_villages)]
    
    # Calculate village-level daily averages
    village_daily = filtered_df.groupby(['Village', 'Days from TPR']).agg({
        'Water Level (mm)': 'mean',
        'Farm ID': 'nunique'
    }).reset_index()
    
    village_daily.rename(columns={'Farm ID': 'Farm Count'}, inplace=True)
    
    # Create village comparison chart
    fig = go.Figure()
    
    colors = px.colors.qualitative.Set3
    
    for i, village in enumerate(selected_villages):
        village_data = village_daily[village_daily['Village'] == village]
        village_data = village_data.sort_values('Days from TPR')
        
        if not village_data.empty:
            fig.add_trace(go.Scatter(
                x=village_data['Days from TPR'],
                y=village_data['Water Level (mm)'],
                mode='lines+markers',
                name=village,
                line=dict(color=colors[i % len(colors)], width=3),
                marker=dict(size=8),
                hovertemplate="<b>%{text}</b><br>" +
                             "Days from TPR: %{x}<br>" +
                             "Avg Water Level: %{y:.1f} mm<br>" +
                             "<extra></extra>",
                text=[village] * len(village_data)
            ))
    
    fig.update_layout(
        title=f"Village-level Water Level Trends Comparison ({len(selected_villages)} villages)",
        xaxis_title="Days from Transplanting",
        yaxis_title="Average Water Level (mm)",
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02
        ),
        height=600,
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Village summary statistics table
    st.markdown("### 📊 Village Summary Statistics")
    
    village_summary = filtered_df.groupby('Village').agg({
        'Water Level (mm)': ['mean', 'std', 'min', 'max', 'count'],
        'Farm ID': 'nunique',
        'Days from TPR': ['min', 'max']
    }).round(2)
    
    # Flatten column names
    village_summary.columns = [
        'Avg Water Level (mm)', 'Std Dev (mm)', 'Min Level (mm)', 
        'Max Level (mm)', 'Total Readings', 'Unique Farms',
        'Min Days from TPR', 'Max Days from TPR'
    ]
    
    village_summary = village_summary.reset_index()
    
    st.dataframe(
        village_summary.style.format({
            'Avg Water Level (mm)': '{:.1f}',
            'Std Dev (mm)': '{:.1f}',
            'Min Level (mm)': '{:.1f}',
            'Max Level (mm)': '{:.1f}'
        }),
        use_container_width=True
    )
    
    # Download village analysis
    csv_buffer = io.StringIO()
    village_summary.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Village Analysis",
        data=csv_buffer.getvalue(),
        file_name=f"village_analysis_{len(selected_villages)}_villages.csv",
        mime="text/csv"
    )

def render_remote_controllers_analysis(merged_df, kharif_df):
    """Remote Controllers: Treatment vs Control (Complied Groups) with selection options"""
    
    st.markdown("### 🎛️ Remote Controllers Study: Treatment vs Control")
    st.markdown("*Comparing complied groups from treatment and control with selection options*")
    
    # Create study group classifications
    study_data = pd.merge(
        merged_df,
        kharif_df[[
            'Kharif 25 Farm ID',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)'
        ]],
        left_on='Farm ID',
        right_on='Kharif 25 Farm ID',
        how='left'
    )
    
    # Define available RC groups
    rc_groups_data = {}
    
    # Treatment groups
    rc_groups_data['Treatment Group (A) - Complied'] = study_data[
        study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'] == 1
    ]
    rc_groups_data['Treatment Group (A) - Non-Complied'] = study_data[
        study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)'] == 1
    ]
    
    # Control groups
    rc_groups_data['Control Group (B) - Complied'] = study_data[
        study_data['Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'] == 1
    ]
    rc_groups_data['Control Group (B) - Non-Complied'] = study_data[
        study_data['Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)'] == 1
    ]
    
    # Filter out empty groups
    available_rc_groups = {k: v for k, v in rc_groups_data.items() if not v.empty}
    
    if not available_rc_groups:
        st.warning("⚠️ No Remote Controllers study data found with compliance information.")
        return
    
    # Group selection options
    st.markdown("#### 📊 Select Remote Controllers Groups for Analysis")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_rc_groups = st.multiselect(
            "Choose RC groups to compare:",
            options=list(available_rc_groups.keys()),
            default=[k for k in available_rc_groups.keys() if 'Complied' in k],  # Default to complied groups
            help="Select which Remote Controllers study groups to include in the comparison"
        )
    
    with col2:
        if selected_rc_groups:
            total_farms = sum([available_rc_groups[group]['Farm ID'].nunique() for group in selected_rc_groups])
            st.metric("Total Farms", total_farms)
            st.metric("Selected Groups", len(selected_rc_groups))
    
    if not selected_rc_groups:
        st.warning("⚠️ Please select at least one Remote Controllers group to analyze.")
        return
    
    # Filter to selected groups
    selected_rc_data = {k: v for k, v in available_rc_groups.items() if k in selected_rc_groups}
    
    # Analysis options
    analysis_option = st.selectbox(
        "📊 Choose Analysis View:",
        options=[
            "Selected Groups Comparison",
            "Treatment vs Control (Selected Groups)",
            "Complied vs Non-Complied (Selected Groups)"
        ]
    )
    
    # Create comparison chart
    fig = go.Figure()
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    if analysis_option == "Selected Groups Comparison":
        # Plot all selected groups individually
        for i, (group_name, group_data) in enumerate(selected_rc_data.items()):
            if not group_data.empty:
                daily_avg = group_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
                daily_avg = daily_avg.sort_values('Days from TPR')
                
                fig.add_trace(go.Scatter(
                    x=daily_avg['Days from TPR'],
                    y=daily_avg['Water Level (mm)'],
                    mode='lines+markers',
                    name=group_name,
                    line=dict(color=colors[i % len(colors)], width=4),
                    marker=dict(size=10),
                    hovertemplate=f"<b>{group_name}</b><br>" +
                                 "Days from TPR: %{x}<br>" +
                                 "Avg Water Level: %{y:.1f} mm<br>" +
                                 "<extra></extra>"
                ))
        
        title = f"Remote Controllers: Selected Groups Comparison ({len(selected_rc_groups)} groups)"
    
    elif analysis_option == "Treatment vs Control (Selected Groups)":
        # Aggregate by treatment vs control
        treatment_data = pd.DataFrame()
        control_data = pd.DataFrame()
        
        for group_name, group_data in selected_rc_data.items():
            if 'Treatment' in group_name:
                treatment_data = pd.concat([treatment_data, group_data])
            elif 'Control' in group_name:
                control_data = pd.concat([control_data, group_data])
        
        # Remove duplicates
        treatment_data = treatment_data.drop_duplicates()
        control_data = control_data.drop_duplicates()
        
        if not treatment_data.empty:
            treatment_daily = treatment_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
            fig.add_trace(go.Scatter(
                x=treatment_daily['Days from TPR'],
                y=treatment_daily['Water Level (mm)'],
                mode='lines+markers',
                name='Treatment Groups (Combined)',
                line=dict(color='blue', width=4),
                marker=dict(size=10)
            ))
        
        if not control_data.empty:
            control_daily = control_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
            fig.add_trace(go.Scatter(
                x=control_daily['Days from TPR'],
                y=control_daily['Water Level (mm)'],
                mode='lines+markers',
                name='Control Groups (Combined)',
                line=dict(color='red', width=4),
                marker=dict(size=10)
            ))
        
        title = "Remote Controllers: Treatment vs Control (Selected Groups)"
    
    else:  # Complied vs Non-Complied
        # Aggregate by compliance status
        complied_data = pd.DataFrame()
        non_complied_data = pd.DataFrame()
        
        for group_name, group_data in selected_rc_data.items():
            if 'Complied' in group_name and 'Non-Complied' not in group_name:
                complied_data = pd.concat([complied_data, group_data])
            elif 'Non-Complied' in group_name:
                non_complied_data = pd.concat([non_complied_data, group_data])
        
        # Remove duplicates
        complied_data = complied_data.drop_duplicates()
        non_complied_data = non_complied_data.drop_duplicates()
        
        if not complied_data.empty:
            complied_daily = complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
            fig.add_trace(go.Scatter(
                x=complied_daily['Days from TPR'],
                y=complied_daily['Water Level (mm)'],
                mode='lines+markers',
                name='Complied Groups (Combined)',
                line=dict(color='green', width=4),
                marker=dict(size=10)
            ))
        
        if not non_complied_data.empty:
            non_complied_daily = non_complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
            fig.add_trace(go.Scatter(
                x=non_complied_daily['Days from TPR'],
                y=non_complied_daily['Water Level (mm)'],
                mode='lines+markers',
                name='Non-Complied Groups (Combined)',
                line=dict(color='red', width=4),
                marker=dict(size=10)
            ))
        
        title = "Remote Controllers: Complied vs Non-Complied (Selected Groups)"
    
    fig.update_layout(
        title=title,
        xaxis_title="Days from Transplanting",
        yaxis_title="Average Water Level (mm)",
        height=500,
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Summary statistics for selected groups
    st.markdown("### 📊 Selected Remote Controllers Groups Statistics")
    
    summary_data = []
    for group_name, group_data in selected_rc_data.items():
        if not group_data.empty:
            summary_data.append({
                'Group': group_name,
                'Farms': group_data['Farm ID'].nunique(),
                'Villages': group_data['Village'].nunique(),
                'Total Readings': len(group_data),
                'Avg Water Level (mm)': round(group_data['Water Level (mm)'].mean(), 1),
                'Std Dev (mm)': round(group_data['Water Level (mm)'].std(), 1),
                'Min Level (mm)': round(group_data['Water Level (mm)'].min(), 1),
                'Max Level (mm)': round(group_data['Water Level (mm)'].max(), 1)
            })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)
        
        # Download options
        st.markdown("### 💾 Download Remote Controllers Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Download summary
            csv_buffer = io.StringIO()
            summary_df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download Summary",
                data=csv_buffer.getvalue(),
                file_name=f"rc_selected_groups_summary_{len(selected_rc_groups)}_groups.csv",
                mime="text/csv"
            )
        
        with col2:
            # Download detailed data
            if st.button("📦 Generate RC Groups Package"):
                zip_buffer = io.BytesIO()
                
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for group_name, group_data in selected_rc_data.items():
                        csv_buffer = io.StringIO()
                        group_data.to_csv(csv_buffer, index=False)
                        safe_name = group_name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
                        zip_file.writestr(f"rc_{safe_name}.csv", csv_buffer.getvalue())
                    
                    # Add summary
                    csv_buffer = io.StringIO()
                    summary_df.to_csv(csv_buffer, index=False)
                    zip_file.writestr("rc_summary.csv", csv_buffer.getvalue())
                
                zip_buffer.seek(0)
                
                st.download_button(
                    label="📦 Download Package (ZIP)",
                    data=zip_buffer.getvalue(),
                    file_name=f"rc_selected_groups_analysis.zip",
                    mime="application/zip"
                )

def render_awd_groups_analysis(merged_df, kharif_df):
    """AWD Study: Groups A, B, C Comparisons (Complied and Non-Complied) with selection options"""
    
    st.markdown("### 💧 AWD Study: Groups A, B, C Comparisons")
    st.markdown("*Analyzing complied and non-complied groups across all AWD study groups*")
    
    # Create study group classifications
    study_data = pd.merge(
        merged_df,
        kharif_df[[
            'Kharif 25 Farm ID',
            'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
            'Kharif 25 - AWD Study - Group B -training only (Y/N)',
            'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
            'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
            'Kharif 25 - AWD Study - Group C - Control (Y/N)',
            'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
            'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
        ]],
        left_on='Farm ID',
        right_on='Kharif 25 Farm ID',
        how='left'
    )
    
    # Create group filters
    groups_data = {}
    
    # Group A - Treatment
    groups_data['Group A (Treatment) - Complied'] = study_data[
        study_data['Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'] == 1
    ]
    groups_data['Group A (Treatment) - Non-Complied'] = study_data[
        study_data['Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)'] == 1
    ]
    
    # Group B - Training
    groups_data['Group B (Training) - Complied'] = study_data[
        study_data['Kharif 25 - AWD Study - Group B - Complied (Y/N)'] == 1
    ]
    groups_data['Group B (Training) - Non-Complied'] = study_data[
        study_data['Kharif 25 - AWD Study - Group B - Non-complied (Y/N)'] == 1
    ]
    
    # Group C - Control
    groups_data['Group C (Control) - Complied'] = study_data[
        study_data['Kharif 25 - AWD Study - Group C - Complied (Y/N)'] == 1
    ]
    groups_data['Group C (Control) - Non-Complied'] = study_data[
        study_data['Kharif 25 - AWD Study - Group C - non-complied (Y/N)'] == 1
    ]
    
    # Filter out empty groups
    available_groups = {k: v for k, v in groups_data.items() if not v.empty}
    
    if not available_groups:
        st.warning("⚠️ No AWD study data found.")
        return
    
    # Group selection options
    st.markdown("#### 📊 Select AWD Groups for Analysis")
    
    # Show available groups with counts
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_groups = st.multiselect(
            "Choose AWD groups to compare:",
            options=list(available_groups.keys()),
            default=list(available_groups.keys())[:3],  # Default to first 3 groups
            help="Select which AWD study groups to include in the comparison"
        )
    
    with col2:
        if selected_groups:
            total_farms = sum([available_groups[group]['Farm ID'].nunique() for group in selected_groups])
            st.metric("Total Farms", total_farms)
            st.metric("Selected Groups", len(selected_groups))
    
    if not selected_groups:
        st.warning("⚠️ Please select at least one AWD group to analyze.")
        return
    
    # Filter to selected groups
    selected_groups_data = {k: v for k, v in available_groups.items() if k in selected_groups}
    
    # Analysis options
    analysis_option = st.selectbox(
        "📊 Choose Analysis View:",
        options=[
            "Selected Groups Comparison",
            "Complied vs Non-Complied (Selected Groups Only)",
            "Group-wise Detailed Analysis"
        ]
    )
    
    if analysis_option == "Selected Groups Comparison":
        # Create comparison chart for selected groups
        fig = go.Figure()
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        
        for i, (group_name, group_data) in enumerate(selected_groups_data.items()):
            if not group_data.empty:
                daily_avg = group_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
                daily_avg = daily_avg.sort_values('Days from TPR')
                
                fig.add_trace(go.Scatter(
                    x=daily_avg['Days from TPR'],
                    y=daily_avg['Water Level (mm)'],
                    mode='lines+markers',
                    name=group_name,
                    line=dict(color=colors[i % len(colors)], width=3),
                    marker=dict(size=8)
                ))
        
        fig.update_layout(
            title=f"AWD Study: Selected Groups Comparison ({len(selected_groups)} groups)",
            xaxis_title="Days from Transplanting",
            yaxis_title="Average Water Level (mm)",
            height=600,
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    elif analysis_option == "Complied vs Non-Complied (Selected Groups Only)":
        # Aggregate complied vs non-complied from selected groups only
        complied_data = pd.DataFrame()
        non_complied_data = pd.DataFrame()
        
        for group_name in selected_groups:
            if 'Complied' in group_name:
                complied_data = pd.concat([complied_data, selected_groups_data[group_name]])
            elif 'Non-Complied' in group_name:
                non_complied_data = pd.concat([non_complied_data, selected_groups_data[group_name]])
        
        # Remove duplicates
        complied_data = complied_data.drop_duplicates()
        non_complied_data = non_complied_data.drop_duplicates()
        
        fig = go.Figure()
        
        if not complied_data.empty:
            complied_daily = complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
            fig.add_trace(go.Scatter(
                x=complied_daily['Days from TPR'],
                y=complied_daily['Water Level (mm)'],
                mode='lines+markers',
                name='Selected Complied Groups',
                line=dict(color='green', width=4),
                marker=dict(size=10)
            ))
        
        if not non_complied_data.empty:
            non_complied_daily = non_complied_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
            fig.add_trace(go.Scatter(
                x=non_complied_daily['Days from TPR'],
                y=non_complied_daily['Water Level (mm)'],
                mode='lines+markers',
                name='Selected Non-Complied Groups',
                line=dict(color='red', width=4),
                marker=dict(size=10)
            ))
        
        fig.update_layout(
            title="AWD Study: Complied vs Non-Complied (Selected Groups)",
            xaxis_title="Days from Transplanting",
            yaxis_title="Average Water Level (mm)",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Summary statistics table for selected groups
    st.markdown("### 📊 Selected AWD Groups Summary Statistics")
    
    summary_data = []
    for group_name, group_data in selected_groups_data.items():
        if not group_data.empty:
            summary_data.append({
                'Group': group_name,
                'Farms': group_data['Farm ID'].nunique(),
                'Villages': group_data['Village'].nunique(),
                'Total Readings': len(group_data),
                'Avg Water Level (mm)': round(group_data['Water Level (mm)'].mean(), 1),
                'Std Dev (mm)': round(group_data['Water Level (mm)'].std(), 1),
                'Min Level (mm)': round(group_data['Water Level (mm)'].min(), 1),
                'Max Level (mm)': round(group_data['Water Level (mm)'].max(), 1)
            })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)
        
        # Download selected groups analysis
        st.markdown("### 💾 Download Selected AWD Groups Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Download summary
            csv_buffer = io.StringIO()
            summary_df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download Summary",
                data=csv_buffer.getvalue(),
                file_name=f"awd_selected_groups_summary_{len(selected_groups)}_groups.csv",
                mime="text/csv"
            )
        
        with col2:
            # Download detailed data
            if st.button("📦 Generate Selected Groups Package"):
                zip_buffer = io.BytesIO()
                
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for group_name, group_data in selected_groups_data.items():
                        csv_buffer = io.StringIO()
                        group_data.to_csv(csv_buffer, index=False)
                        safe_name = group_name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
                        zip_file.writestr(f"awd_{safe_name}.csv", csv_buffer.getvalue())
                    
                    # Add summary
                    csv_buffer = io.StringIO()
                    summary_df.to_csv(csv_buffer, index=False)
                    zip_file.writestr("awd_summary.csv", csv_buffer.getvalue())
                
                zip_buffer.seek(0)
                
                st.download_button(
                    label="📦 Download Package (ZIP)",
                    data=zip_buffer.getvalue(),
                    file_name=f"awd_selected_groups_analysis.zip",
                    mime="application/zip"
                )

def render_dsr_tpr_analysis(merged_df, kharif_df):
    """DSR vs TPR Group Comparisons"""
    
    st.markdown("### 🌱 DSR vs TPR Farming Methods Comparison")
    st.markdown("*Comparing Direct Seeded Rice vs Transplanted Rice methods*")
    
    # Create study group classifications
    study_data = pd.merge(
        merged_df,
        kharif_df[[
            'Kharif 25 Farm ID',
            'Kharif 25 - DSR farm Study (Y/N)',
            'Kharif 25 - TPR Group Study (Y/N)'
        ]],
        left_on='Farm ID',
        right_on='Kharif 25 Farm ID',
        how='left'
    )
    
    # Filter for each method
    dsr_farms = study_data[study_data['Kharif 25 - DSR farm Study (Y/N)'] == 1]
    tpr_farms = study_data[study_data['Kharif 25 - TPR Group Study (Y/N)'] == 1]
    
    if dsr_farms.empty and tpr_farms.empty:
        st.warning("⚠️ No DSR or TPR study data found.")
        return
    
    # Create comparison chart
    fig = go.Figure()
    
    if not dsr_farms.empty:
        dsr_daily = dsr_farms.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
        dsr_daily = dsr_daily.sort_values('Days from TPR')
        
        fig.add_trace(go.Scatter(
            x=dsr_daily['Days from TPR'],
            y=dsr_daily['Water Level (mm)'],
            mode='lines+markers',
            name='DSR (Direct Seeded Rice)',
            line=dict(color='green', width=4),
            marker=dict(size=10, symbol='circle'),
            hovertemplate="<b>DSR Method</b><br>" +
                         "Days from TPR: %{x}<br>" +
                         "Avg Water Level: %{y:.1f} mm<br>" +
                         "<extra></extra>"
        ))
    
    if not tpr_farms.empty:
        tpr_daily = tpr_farms.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
        tpr_daily = tpr_daily.sort_values('Days from TPR')
        
        fig.add_trace(go.Scatter(
            x=tpr_daily['Days from TPR'],
            y=tpr_daily['Water Level (mm)'],
            mode='lines+markers',
            name='TPR (Transplanted Rice)',
            line=dict(color='blue', width=4),
            marker=dict(size=10, symbol='diamond'),
            hovertemplate="<b>TPR Method</b><br>" +
                         "Days from TPR: %{x}<br>" +
                         "Avg Water Level: %{y:.1f} mm<br>" +
                         "<extra></extra>"
        ))
    
    fig.update_layout(
        title="Farming Methods Comparison: DSR vs TPR",
        xaxis_title="Days from Transplanting/Seeding",
        yaxis_title="Average Water Level (mm)",
        height=500,
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Comparative statistics
    st.markdown("### 📊 Method Comparison Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not dsr_farms.empty:
            st.markdown("**DSR (Direct Seeded Rice):**")
            st.metric("👥 Farms", dsr_farms['Farm ID'].nunique())
            st.metric("📊 Avg Water Level", f"{dsr_farms['Water Level (mm)'].mean():.1f} mm")
            st.metric("📏 Std Deviation", f"{dsr_farms['Water Level (mm)'].std():.1f} mm")
            st.metric("📈 Total Readings", len(dsr_farms))
    
    with col2:
        if not tpr_farms.empty:
            st.markdown("**TPR (Transplanted Rice):**")
            st.metric("👥 Farms", tpr_farms['Farm ID'].nunique())
            st.metric("📊 Avg Water Level", f"{tpr_farms['Water Level (mm)'].mean():.1f} mm")
            st.metric("📏 Std Deviation", f"{tpr_farms['Water Level (mm)'].std():.1f} mm")
            st.metric("📈 Total Readings", len(tpr_farms))

def render_compliance_analysis(merged_df, kharif_df):
    """Comprehensive Compliance Analysis"""
    
    st.markdown("### ✅ Comprehensive Compliance Analysis")
    st.markdown("*Analyzing compliance rates across all studies*")
    
    # Create comprehensive study classifications
    study_data = pd.merge(
        merged_df,
        kharif_df[[
            'Kharif 25 Farm ID',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment - NON-complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control - NON-complied (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment - Non-complied (Y/N)',
            'Kharif 25 - AWD Study - Group B -training only (Y/N)',
            'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
            'Kharif 25 - AWD Study - Group B - Non-complied (Y/N)',
            'Kharif 25 - AWD Study - Group C - Control (Y/N)',
            'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
            'Kharif 25 - AWD Study - Group C - non-complied (Y/N)'
        ]],
        left_on='Farm ID',
        right_on='Kharif 25 Farm ID',
        how='left'
    )
    
    # Calculate compliance rates
    compliance_data = []
    
    # Remote Controllers compliance
    studies = [
        {
            'study': 'Remote Controllers - Treatment (A)',
            'total_col': 'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
            'complied_col': 'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'
        },
        {
            'study': 'Remote Controllers - Control (B)',
            'total_col': 'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
            'complied_col': 'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'
        },
        {
            'study': 'AWD - Group A (Treatment)',
            'total_col': 'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
            'complied_col': 'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'
        },
        {
            'study': 'AWD - Group B (Training)',
            'total_col': 'Kharif 25 - AWD Study - Group B -training only (Y/N)',
            'complied_col': 'Kharif 25 - AWD Study - Group B - Complied (Y/N)'
        },
        {
            'study': 'AWD - Group C (Control)',
            'total_col': 'Kharif 25 - AWD Study - Group C - Control (Y/N)',
            'complied_col': 'Kharif 25 - AWD Study - Group C - Complied (Y/N)'
        }
    ]
    
    for study_info in studies:
        total_farms = len(study_data[study_data[study_info['total_col']] == 1]['Farm ID'].unique())
        complied_farms = len(study_data[study_data[study_info['complied_col']] == 1]['Farm ID'].unique())
        
        if total_farms > 0:
            compliance_rate = (complied_farms / total_farms) * 100
            compliance_data.append({
                'Study Group': study_info['study'],
                'Total Farms': total_farms,
                'Complied Farms': complied_farms,
                'Non-Complied Farms': total_farms - complied_farms,
                'Compliance Rate (%)': round(compliance_rate, 1)
            })
    
    if not compliance_data:
        st.warning("⚠️ No compliance data found.")
        return
    
    # Display compliance table
    compliance_df = pd.DataFrame(compliance_data)
    st.dataframe(compliance_df, use_container_width=True)
    
    # Compliance visualization
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=compliance_df['Study Group'],
        y=compliance_df['Compliance Rate (%)'],
        text=compliance_df['Compliance Rate (%)'].apply(lambda x: f"{x:.1f}%"),
        textposition='auto',
        marker_color='lightblue',
        name='Compliance Rate'
    ))
    
    fig.update_layout(
        title="Compliance Rates Across All Studies",
        xaxis_title="Study Groups",
        yaxis_title="Compliance Rate (%)",
        height=400,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed compliance analysis
    st.markdown("### 📊 Detailed Compliance Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Overall compliance metrics
        total_participants = compliance_df['Total Farms'].sum()
        total_complied = compliance_df['Complied Farms'].sum()
        overall_compliance = (total_complied / total_participants) * 100 if total_participants > 0 else 0
        
        st.metric("🎯 Overall Compliance Rate", f"{overall_compliance:.1f}%")
        st.metric("👥 Total Participating Farms", total_participants)
        st.metric("✅ Total Complied Farms", total_complied)
    
    with col2:
        # Best and worst performing groups
        if not compliance_df.empty:
            best_group = compliance_df.loc[compliance_df['Compliance Rate (%)'].idxmax()]
            worst_group = compliance_df.loc[compliance_df['Compliance Rate (%)'].idxmin()]
            
            st.success(f"🏆 Best Compliance: {best_group['Study Group']} ({best_group['Compliance Rate (%)']}%)")
            st.error(f"⚠️ Lowest Compliance: {worst_group['Study Group']} ({worst_group['Compliance Rate (%)']}%)")

def render_custom_selection_analysis(merged_df, kharif_df):
    """Custom village and farm selection for flexible analysis"""
    
    st.markdown("### 🎯 Custom Village/Farm Selection Analysis")
    st.markdown("*Create custom groups by selecting specific villages and farms*")
    
    if merged_df.empty:
        st.warning("⚠️ No data available for custom analysis.")
        return
    
    # Selection method
    selection_method = st.radio(
        "📊 Choose Selection Method:",
        options=["Select by Villages", "Select by Farms", "Mixed Selection (Villages + Farms)"],
        horizontal=True
    )
    
    custom_groups = {}
    
    if selection_method == "Select by Villages":
        st.markdown("#### 🏘️ Village-based Group Creation")
        
        available_villages = sorted(merged_df['Village'].unique())
        
        # Allow creation of multiple village groups
        num_groups = st.number_input("Number of village groups to create:", min_value=1, max_value=5, value=2)
        
        for i in range(num_groups):
            st.markdown(f"**Group {i+1}:**")
            col1, col2 = st.columns([3, 1])
            
            with col1:
                group_villages = st.multiselect(
                    f"Select villages for Group {i+1}:",
                    options=available_villages,
                    key=f"village_group_{i}",
                    help=f"Choose villages to include in Group {i+1}"
                )
            
            with col2:
                if group_villages:
                    group_data = merged_df[merged_df['Village'].isin(group_villages)]
                    st.metric("Farms", group_data['Farm ID'].nunique())
                    st.metric("Records", len(group_data))
            
            if group_villages:
                group_name = f"Village Group {i+1} ({', '.join(group_villages[:2])}{'...' if len(group_villages) > 2 else ''})"
                custom_groups[group_name] = merged_df[merged_df['Village'].isin(group_villages)]
    
    elif selection_method == "Select by Farms":
        st.markdown("#### 🏡 Farm-based Group Creation")
        
        available_farms = sorted(merged_df['Farm ID'].unique())
        
        # Show farms with their villages for context
        farm_village_map = merged_df[['Farm ID', 'Village']].drop_duplicates().set_index('Farm ID')['Village'].to_dict()
        
        # Allow creation of multiple farm groups
        num_groups = st.number_input("Number of farm groups to create:", min_value=1, max_value=5, value=2)
        
        for i in range(num_groups):
            st.markdown(f"**Group {i+1}:**")
            col1, col2 = st.columns([3, 1])
            
            with col1:
                group_farms = st.multiselect(
                    f"Select farms for Group {i+1}:",
                    options=available_farms,
                    format_func=lambda x: f"{x} ({farm_village_map.get(x, 'Unknown Village')})",
                    key=f"farm_group_{i}",
                    help=f"Choose farms to include in Group {i+1}"
                )
            
            with col2:
                if group_farms:
                    group_data = merged_df[merged_df['Farm ID'].isin(group_farms)]
                    st.metric("Villages", group_data['Village'].nunique())
                    st.metric("Records", len(group_data))
            
            if group_farms:
                group_name = f"Farm Group {i+1} ({len(group_farms)} farms)"
                custom_groups[group_name] = merged_df[merged_df['Farm ID'].isin(group_farms)]
    
    else:  # Mixed Selection
        st.markdown("#### 🎯 Mixed Village + Farm Selection")
        
        available_villages = sorted(merged_df['Village'].unique())
        available_farms = sorted(merged_df['Farm ID'].unique())
        farm_village_map = merged_df[['Farm ID', 'Village']].drop_duplicates().set_index('Farm ID')['Village'].to_dict()
        
        # Allow creation of multiple mixed groups
        num_groups = st.number_input("Number of mixed groups to create:", min_value=1, max_value=3, value=2)
        
        for i in range(num_groups):
            st.markdown(f"**Mixed Group {i+1}:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("*Select Villages:*")
                group_villages = st.multiselect(
                    f"Villages for Group {i+1}:",
                    options=available_villages,
                    key=f"mixed_villages_{i}"
                )
            
            with col2:
                st.markdown("*Select Additional Farms:*")
                group_farms = st.multiselect(
                    f"Additional farms for Group {i+1}:",
                    options=available_farms,
                    format_func=lambda x: f"{x} ({farm_village_map.get(x, 'Unknown')})",
                    key=f"mixed_farms_{i}"
                )
            
            # Combine village and farm selections
            if group_villages or group_farms:
                group_data = pd.DataFrame()
                
                if group_villages:
                    village_data = merged_df[merged_df['Village'].isin(group_villages)]
                    group_data = pd.concat([group_data, village_data])
                
                if group_farms:
                    farm_data = merged_df[merged_df['Farm ID'].isin(group_farms)]
                    group_data = pd.concat([group_data, farm_data])
                
                # Remove duplicates
                group_data = group_data.drop_duplicates()
                
                if not group_data.empty:
                    group_name = f"Mixed Group {i+1}"
                    custom_groups[group_name] = group_data
                    
                    # Show group summary
                    col3, col4, col5 = st.columns(3)
                    with col3:
                        st.metric("Total Farms", group_data['Farm ID'].nunique())
                    with col4:
                        st.metric("Villages", group_data['Village'].nunique())
                    with col5:
                        st.metric("Records", len(group_data))
    
    # Analysis and visualization of custom groups
    if custom_groups:
        st.markdown("---")
        st.markdown("### 📊 Custom Groups Analysis")
        
        # Create comparison chart
        fig = go.Figure()
        colors = px.colors.qualitative.Set3
        
        for i, (group_name, group_data) in enumerate(custom_groups.items()):
            if not group_data.empty:
                # Calculate daily averages for the group
                daily_avg = group_data.groupby('Days from TPR')['Water Level (mm)'].mean().reset_index()
                daily_avg = daily_avg.sort_values('Days from TPR')
                
                fig.add_trace(go.Scatter(
                    x=daily_avg['Days from TPR'],
                    y=daily_avg['Water Level (mm)'],
                    mode='lines+markers',
                    name=group_name,
                    line=dict(color=colors[i % len(colors)], width=3),
                    marker=dict(size=8),
                    hovertemplate=f"<b>{group_name}</b><br>" +
                                 "Days from TPR: %{x}<br>" +
                                 "Avg Water Level: %{y:.1f} mm<br>" +
                                 "<extra></extra>"
                ))
        
        fig.update_layout(
            title=f"Custom Groups Comparison ({len(custom_groups)} groups)",
            xaxis_title="Days from Transplanting",
            yaxis_title="Average Water Level (mm)",
            height=600,
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Summary statistics table
        st.markdown("### 📋 Custom Groups Summary")
        
        summary_data = []
        for group_name, group_data in custom_groups.items():
            if not group_data.empty:
                summary_data.append({
                    'Group': group_name,
                    'Farms': group_data['Farm ID'].nunique(),
                    'Villages': group_data['Village'].nunique(),
                    'Total Readings': len(group_data),
                    'Avg Water Level (mm)': round(group_data['Water Level (mm)'].mean(), 1),
                    'Std Dev (mm)': round(group_data['Water Level (mm)'].std(), 1),
                    'Date Range': f"{group_data['Date'].min().strftime('%Y-%m-%d')} to {group_data['Date'].max().strftime('%Y-%m-%d')}"
                })
        
        if summary_data:
            summary_df = pd.DataFrame(summary_data)
            st.dataframe(summary_df, use_container_width=True)
            
            # Download options for custom analysis
            st.markdown("### 💾 Download Custom Analysis")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Download summary
                csv_buffer = io.StringIO()
                summary_df.to_csv(csv_buffer, index=False)
                st.download_button(
                    label="📥 Download Summary",
                    data=csv_buffer.getvalue(),
                    file_name="custom_groups_summary.csv",
                    mime="text/csv"
                )
            
            with col2:
                # Download detailed data for all groups
                if st.button("📦 Generate Detailed Data Package"):
                    zip_buffer = io.BytesIO()
                    
                    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                        for group_name, group_data in custom_groups.items():
                            csv_buffer = io.StringIO()
                            group_data.to_csv(csv_buffer, index=False)
                            safe_name = group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')
                            zip_file.writestr(f"{safe_name}_data.csv", csv_buffer.getvalue())
                        
                        # Add summary
                        csv_buffer = io.StringIO()
                        summary_df.to_csv(csv_buffer, index=False)
                        zip_file.writestr("summary.csv", csv_buffer.getvalue())
                    
                    zip_buffer.seek(0)
                    
                    st.download_button(
                        label="📦 Download All Groups (ZIP)",
                        data=zip_buffer.getvalue(),
                        file_name="custom_groups_analysis.zip",
                        mime="application/zip"
                    )
    
    else:
        st.info("👆 Please select villages or farms above to create custom groups for analysis.")
        
        # Show quick stats about available data
        with st.expander("📊 Available Data Overview"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Villages", merged_df['Village'].nunique())
                st.metric("Total Farms", merged_df['Farm ID'].nunique())
            
            with col2:
                st.metric("Total Records", len(merged_df))
                st.metric("Date Range", f"{(merged_df['Date'].max() - merged_df['Date'].min()).days} days")
            
            with col3:
                avg_water = merged_df['Water Level (mm)'].mean()
                std_water = merged_df['Water Level (mm)'].std()
                st.metric("Avg Water Level", f"{avg_water:.1f} mm")
                st.metric("Std Deviation", f"{std_water:.1f} mm")

def create_comprehensive_downloads(merged_df, kharif_df, farm_daily_avg, weekly_avg):
    """Create comprehensive download section with all data exports"""
    
    st.markdown('<div class="section-header">💾 Comprehensive Data Downloads</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Available Data Exports")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📊 Complete Datasets**")
        
        # Complete merged dataset
        csv_buffer = io.StringIO()
        merged_df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Complete Merged Dataset",
            data=csv_buffer.getvalue(),
            file_name="complete_merged_agricultural_data.csv",
            mime="text/csv",
            help="All water level data merged with farm information"
        )
        
        # Raw Kharif data
        csv_buffer = io.StringIO()
        kharif_df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Raw Kharif Data",
            data=csv_buffer.getvalue(),
            file_name="raw_kharif_farm_data.csv",
            mime="text/csv",
            help="Original farm and study group data"
        )
    
    with col2:
        st.markdown("**👥 Study Group Data**")
        
        # Create study group datasets
        study_groups = create_study_group_datasets(merged_df, kharif_df)
        
        for group_name, group_data in study_groups.items():
            if not group_data.empty:
                csv_buffer = io.StringIO()
                group_data.to_csv(csv_buffer, index=False)
                st.download_button(
                    label=f"📥 {group_name}",
                    data=csv_buffer.getvalue(),
                    file_name=f"{group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}_data.csv",
                    mime="text/csv",
                    help=f"Data for {group_name} participants"
                )
    
    with col3:
        st.markdown("**📈 Analysis Reports**")
        
        # Village summary
        if 'Village' in merged_df.columns:
            village_summary = merged_df.groupby('Village').agg({
                'Water Level (mm)': ['mean', 'std', 'count'],
                'Farm ID': 'nunique'
            }).round(2)
            village_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Unique Farms']
            
            csv_buffer = io.StringIO()
            village_summary.to_csv(csv_buffer)
            st.download_button(
                label="📥 Village Summary",
                data=csv_buffer.getvalue(),
                file_name="village_summary_report.csv",
                mime="text/csv",
                help="Statistical summary by village"
            )
        
        # Farm summary
        farm_summary = merged_df.groupby('Farm ID').agg({
            'Water Level (mm)': ['mean', 'std', 'count'],
            'Days from TPR': ['min', 'max']
        }).round(2)
        farm_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Min Days', 'Max Days']
        
        csv_buffer = io.StringIO()
        farm_summary.to_csv(csv_buffer)
        st.download_button(
            label="📥 Farm Summary",
            data=csv_buffer.getvalue(),
            file_name="farm_summary_report.csv",
            mime="text/csv",
            help="Statistical summary by farm"
        )
    
    # Create comprehensive ZIP download
    st.markdown("### 📦 Complete Data Package")
    st.markdown("*Download all datasets and reports in a single ZIP file*")
    
    if st.button("🗜️ Generate Complete Data Package", help="Create ZIP file with all data"):
        create_zip_package(merged_df, kharif_df, farm_daily_avg, weekly_avg)

def create_study_group_datasets(merged_df, kharif_df):
    """Create datasets for each study group"""
    
    # Merge for study group classifications
    study_data = pd.merge(
        merged_df,
        kharif_df[[
            'Kharif 25 Farm ID',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control Group (Y/N)',
            'Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment (Y/N)',
            'Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)',
            'Kharif 25 - AWD Study - Group B -training only (Y/N)',
            'Kharif 25 - AWD Study - Group B - Complied (Y/N)',
            'Kharif 25 - AWD Study - Group C - Control (Y/N)',
            'Kharif 25 - AWD Study - Group C - Complied (Y/N)',
            'Kharif 25 - TPR Group Study (Y/N)',
            'Kharif 25 - DSR farm Study (Y/N)'
        ]],
        left_on='Farm ID',
        right_on='Kharif 25 Farm ID',
        how='left'
    )
    
    study_groups = {}
    
    # Remote Controllers groups
    rc_treatment = study_data[study_data['Kharif 25 - Remote Controllers Study - Group A - Treatment - complied (Y/N)'] == 1]
    if not rc_treatment.empty:
        study_groups['Remote Controllers Treatment'] = rc_treatment
    
    rc_control = study_data[study_data['Kharif 25 - Remote Controllers Study - Group B - Control - complied (Y/N)'] == 1]
    if not rc_control.empty:
        study_groups['Remote Controllers Control'] = rc_control
    
    # AWD groups
    awd_a = study_data[study_data['Kharif 25 - AWD Study - Group A - Treatment - complied (Y/N)'] == 1]
    if not awd_a.empty:
        study_groups['AWD Group A Treatment'] = awd_a
    
    awd_b = study_data[study_data['Kharif 25 - AWD Study - Group B - Complied (Y/N)'] == 1]
    if not awd_b.empty:
        study_groups['AWD Group B Training'] = awd_b
    
    awd_c = study_data[study_data['Kharif 25 - AWD Study - Group C - Complied (Y/N)'] == 1]
    if not awd_c.empty:
        study_groups['AWD Group C Control'] = awd_c
    
    # Farming methods
    dsr_group = study_data[study_data['Kharif 25 - DSR farm Study (Y/N)'] == 1]
    if not dsr_group.empty:
        study_groups['DSR Farms'] = dsr_group
    
    tpr_group = study_data[study_data['Kharif 25 - TPR Group Study (Y/N)'] == 1]
    if not tpr_group.empty:
        study_groups['TPR Farms'] = tpr_group
    
    return study_groups

def create_zip_package(merged_df, kharif_df, farm_daily_avg, weekly_avg):
    """Create comprehensive ZIP package with all data"""
    
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        
        # Add main datasets
        csv_buffer = io.StringIO()
        merged_df.to_csv(csv_buffer, index=False)
        zip_file.writestr("01_complete_merged_data.csv", csv_buffer.getvalue())
        
        csv_buffer = io.StringIO()
        kharif_df.to_csv(csv_buffer, index=False)
        zip_file.writestr("02_raw_kharif_data.csv", csv_buffer.getvalue())
        
        # Add processed datasets
        if not farm_daily_avg.empty:
            csv_buffer = io.StringIO()
            farm_daily_avg.to_csv(csv_buffer, index=False)
            zip_file.writestr("03_farm_daily_averages.csv", csv_buffer.getvalue())
        
        if not weekly_avg.empty:
            csv_buffer = io.StringIO()
            weekly_avg.to_csv(csv_buffer, index=False)
            zip_file.writestr("04_weekly_averages.csv", csv_buffer.getvalue())
        
        # Add study group datasets
        study_groups = create_study_group_datasets(merged_df, kharif_df)
        for i, (group_name, group_data) in enumerate(study_groups.items(), 5):
            if not group_data.empty:
                csv_buffer = io.StringIO()
                group_data.to_csv(csv_buffer, index=False)
                filename = f"{i:02d}_{group_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.csv"
                zip_file.writestr(filename, csv_buffer.getvalue())
        
        # Add summary reports
        if 'Village' in merged_df.columns:
            village_summary = merged_df.groupby('Village').agg({
                'Water Level (mm)': ['mean', 'std', 'count'],
                'Farm ID': 'nunique'
            }).round(2)
            village_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Unique Farms']
            
            csv_buffer = io.StringIO()
            village_summary.to_csv(csv_buffer)
            zip_file.writestr("20_village_summary.csv", csv_buffer.getvalue())
        
        farm_summary = merged_df.groupby('Farm ID').agg({
            'Water Level (mm)': ['mean', 'std', 'count'],
            'Days from TPR': ['min', 'max']
        }).round(2)
        farm_summary.columns = ['Avg Water Level', 'Std Dev', 'Total Readings', 'Min Days', 'Max Days']
        
        csv_buffer = io.StringIO()
        farm_summary.to_csv(csv_buffer)
        zip_file.writestr("21_farm_summary.csv", csv_buffer.getvalue())
        
        # Add README
        readme_content = """
Agricultural Data Analysis Package
=================================

This package contains:

Main Datasets:
- 01_complete_merged_data.csv: All water level data merged with farm information
- 02_raw_kharif_data.csv: Original farm and study group data
- 03_farm_daily_averages.csv: Daily averages per farm
- 04_weekly_averages.csv: Weekly averages per farm

Study Groups:
- Remote Controllers Treatment/Control groups
- AWD Study Groups A, B, C
- DSR and TPR farming method groups

Summary Reports:
- 20_village_summary.csv: Statistics by village
- 21_farm_summary.csv: Statistics by farm

Generated on: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        zip_file.writestr("README.txt", readme_content)
    
    zip_buffer.seek(0)
    
    st.download_button(
        label="📦 Download Complete Package (ZIP)",
        data=zip_buffer.getvalue(),
        file_name=f"agricultural_data_complete_package_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
        mime="application/zip",
        help="Complete package with all datasets and reports"
    )

def main():
    """Enhanced main function with complete dashboard functionality"""
    
    # Main title
    st.markdown('<div class="main-header">🌾 Enhanced Agricultural Data Analysis Dashboard</div>', unsafe_allow_html=True)
    st.markdown("*Comprehensive analysis with advanced filtering, comparisons, and enhanced downloads*")
    
    # Add navigation to 2024 analysis
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button("🔗 Analyze 2024 Data", "https://v45bgthcmmrztmbstkddra.streamlit.app/", use_container_width=True)
    
    st.markdown("---")
    
    # Load and validate data
    kharif_df, water_df = load_and_validate_data()
    
    if kharif_df is not None and water_df is not None:
        
        # Data processing with progress indicator
        with st.spinner("🔄 Processing and cleaning data..."):
            kharif_cleaned, water_cleaned = clean_and_process_data(kharif_df, water_df)
            
            # Create filters
            filters = create_advanced_filters(kharif_cleaned, water_cleaned)
            
            # Apply filters
            filtered_kharif, filtered_water = apply_comprehensive_filters(kharif_cleaned, water_cleaned, filters)
            
            # Create merged dataset
            merged_df, farm_daily_avg, weekly_avg = create_merged_dataset(filtered_kharif, filtered_water)
        
        # Display data overview in sidebar
        with st.sidebar:
            st.markdown('<div class="section-header">📊 Data Overview</div>', unsafe_allow_html=True)
            
            st.markdown(f"""
            **📈 Current Dataset:**
            - **Merged Records:** {len(merged_df):,}
            - **Unique Farms:** {merged_df['Farm ID'].nunique() if not merged_df.empty else 0:,}
            - **Villages:** {merged_df['Village'].nunique() if 'Village' in merged_df.columns and not merged_df.empty else 0:,}
            - **Date Range:** {merged_df['Date'].min().strftime('%Y-%m-%d') if not merged_df.empty else 'N/A'} to {merged_df['Date'].max().strftime('%Y-%m-%d') if not merged_df.empty else 'N/A'}
            """)
            
            if not merged_df.empty:
                avg_water_level = merged_df['Water Level (mm)'].mean()
                st.markdown(f"- **Avg Water Level:** {avg_water_level:.1f} mm")
            
            st.markdown("---")
            st.markdown("**📋 Original Data:**")
            st.markdown(f"- **Kharif Records:** {len(kharif_df):,}")
            st.markdown(f"- **Water Records:** {len(water_df):,}")
        
        if merged_df.empty:
            st.warning("⚠️ No data available after applying filters. Please adjust your filter settings.")
            
            with st.expander("🔧 Troubleshooting Tips"):
                st.markdown("""
                **Common Issues:**
                - **Date Range:** Ensure selected dates overlap with your data
                - **Village Names:** Check for typos or variations in village names
                - **Study Groups:** Verify that selected groups have data
                - **Farm IDs:** Ensure farm IDs match between datasets
                
                **Try:**
                - Reset filters to "All" options
                - Check the original data structure
                - Expand date range selection
                """)
        else:
            st.success(f"✅ Successfully processed {len(merged_df):,} records from {merged_df['Farm ID'].nunique()} farms!")
            
            # Create main tabs
            tab1, tab2, tab3 = st.tabs([
                "🏡 Individual Farm Analysis",
                "👥 Comparative Analysis",
                "💾 Data Downloads"
            ])
            
            with tab1:
                render_individual_farm_analysis(merged_df, farm_daily_avg, weekly_avg)
            
            with tab2:
                render_comparative_analysis(merged_df, filtered_kharif)
            
            with tab3:
                create_comprehensive_downloads(merged_df, filtered_kharif, farm_daily_avg, weekly_avg)
    
    else:
        # Data upload instructions
        st.info("📁 Please upload both Excel files to begin analysis.")
        
        with st.expander("ℹ️ Expected Data Structure & Features", expanded=True):
            st.markdown("""
            ### 📋 Required Files:
            
            **1. Kharif 25 Excel File:**
            - `Kharif 25 Farm ID` - Unique farm identifier
            - `Kharif 25 Village` - Village name
            - `Kharif 25 Paddy transplanting date (TPR)` - Transplanting date
            - Study group columns (Remote Controllers, AWD, TPR, DSR)
            - PVC Pipe codes (1-5)
            - Compliance indicators (Y/N)
            
            **2. Water Level Measurement Excel File:**
            - `Date` - Measurement date
            - `Farm ID` - Farm identifier (must match Kharif file)
            - `Pipe code ID of the farm` - Pipe identifier
            - `Measure water level inside the PVC pipe - millimeter mm` - Water level reading
            - `Village name` - Village name
            
            ### ✨ Enhanced Features:
            
            **🔍 Advanced Filters:**
            - 📅 Date range selection with validation
            - 🏘️ Village-specific filtering with typo handling
            - 🔬 Study group filtering (RC, AWD, TPR, DSR)
            - ✅ Compliance status filtering
            - 🔧 Data quality filters (minimum readings, outlier removal)
            
            **📊 Complete Analysis:**
            - **Graph 1:** Daily water levels per pipe + farm average (markers only)
            - **Graph 2:** Weekly water level trends (markers + farm average line)
            - **Table 3:** Water level data with Days from TPR as Column A
            - **Comparative Charts:** All required study group comparisons
            
            **👥 Study Group Comparisons:**
            - Remote Controllers: Treatment vs Control (complied groups)
            - AWD Study: Groups A, B, C (complied and non-complied)
            - DSR vs TPR group comparisons
            - Village-level aggregations
            - Comprehensive compliance analysis
            
            **💾 Enhanced Downloads:**
            - Individual farm reports (detailed + summary)
            - Study group datasets (separate CSV files)
            - Village and farm summary reports
            - Complete data packages (ZIP format)
            
            **🔧 Data Quality Features:**
            - Fuzzy matching for village names (handles typos)
            - Case insensitive comparisons
            - Data normalization and cleaning
            - Outlier detection and removal
            - Missing data handling
            
            **📈 Advanced Visualizations:**
            - Interactive charts with hover information
            - Color-coded study groups
            - Responsive design for all screen sizes
            - Export-ready chart formats
            """)

if __name__ == "__main__":
    main()