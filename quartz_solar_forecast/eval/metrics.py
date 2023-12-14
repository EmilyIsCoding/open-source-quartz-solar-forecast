def metrics(results_df):
    """
    Calculate and print metrics: MAE

    results_df dataframe with the following columns
    - timestamp
    - pv_id
    - horizon_hours
    - forecast_power
    - generation_power

    """

    mae = (results_df["forecast_power"] - results_df['generation_power']).abs().mean().round(4)
    print(f"MAE: {mae}")

    # calculate metrics over the different horizons hours
    # find all unique horizon_hours
    horizon_hours = results_df["horizon_hour"].unique()
    for horizon_hour in horizon_hours:
        # filter results_df to only include the horizon_hour
        results_df_horizon = results_df[results_df["horizon_hour"] == horizon_hour]
        mae = (results_df_horizon["forecast_power"] - results_df_horizon['generation_power']).abs().mean().round(3)
        sem = ((results_df_horizon["forecast_power"] - results_df_horizon['generation_power']).abs().std() / len(results_df_horizon)**0.5).round(3)

        print(f"MAE for horizon {horizon_hour}: {mae} +- {1.96*sem}")

    # TODO add more metrics using ocf_ml_metrics



