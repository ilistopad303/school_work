# Import required packages for data manipulation, visualization, and statistical analysis
using DataFrames, CSV, Plots, Dates, Statistics, StatsBase, StatsPlots, GLM, Chain

"""
Task 1: Load and preprocess S&P 500 stock price data
"""
function load_and_preprocess_data(filepath, numeric_columns)
    # Load CSV data into a DataFrame structure
    df = DataFrame(CSV.read(filepath, DataFrame))
    #Round Each column to two decimal places
    for (col) in (numeric_columns)
        if (col) in (names(df))
            df[!, col] = round.(df[!, col]; digits=2)
        end
    end
    
    return df
    return numeric_columns
end

"""
Task 2: Normalize numerical columns using min-max scaling
"""
function normalize_numerical_columns!(df, numeric_columns)
    # Get names of all numeric columns in the DataFrame
    for col in numeric_columns
        col_min = minimum(skipmissing(df[!, col]))
        col_max = maximum(skipmissing(df[!, col]))
        # TODO: Implement min-max scaling formula
        df[!, col] = (df[!, col] .- col_min) ./ (col_max - col_min)
    end
end

"""
Task 3: Create time-based features and filter data
"""
function process_time_features!(df)
    # TODO: Add time-based columns (Year, Month, Quarter)
    # Extract year, month, and quarter from the Date column
    df.Year = year.(df.Date)
    df.Month = month.(df.Date)
    df.Quarter = quarterofyear.(df.Date)
    # # Filter DataFrame to keep only rows between 2014-2022
    filter!(row -> 2014 <= (row.Year) <= 2022, df)
end

"""
Task 4: Calculate aggregated statistics
"""
function calculate_statistics(df)
    # TODO: Calculate yearly aggregated statistics using combine and groupby operations
    yearly_stats = combine(groupby(df, :Year), 
        :SP500 => mean => :Mean_SP500,
        :Dividend => mean => :Mean_Dividend,
        :Earnings => mean => :Mean_Earnings,
        :"Consumer Price Index" => mean => :Mean_ConsumerPriceIndex,
        :"Long Interest Rate" => mean => :Average_LongInterestRate,
        :"Real Price" => mean => :Average_RealPrice,
        :"Real Dividend" => mean => :Average_RealDividend,
        :"Real Earnings" => mean => :Average_RealEarnings,
        :PE10 => mean => :Average_PE10
    )
    
    # Calculate sum of dividends by month
    monthly_stats = combine(groupby(df, :Month), :Dividend => sum)
    # Calculate sum of dividends by quarter
    quarterly_stats = combine(groupby(df, :Quarter), :Dividend => sum)
    return yearly_stats, monthly_stats, quarterly_stats
end

"""
Task 5A: Create 1D visualizations
"""
function create_visualizations(df)
    # TODO: Create three different types of plots for data visualization
    p1 = boxplot(df.Year, df[!, "Real Price"], title="Boxplot of Real Price per year", linewidth = 2)
    p2 = histogram(df[!, "Earnings"], bins=20, title="Histogram of Earnings", xlabel="Earnings", ylabel="Frequency", legend=false)
    p3 = scatter(df[!, "PE10"], df[!, "Real Price"], title="PE10 vs Real Price", xlabel="PE10", ylabel="Real Price", legend=false)
    
    # Combine all three plots into a single figure
    combined_plot = plot(p1, p2, p3, layout=(1,3), size=(1200,400))
    # Save the combined visualization to a PNG file
    savefig(combined_plot, "multiple-visualization.png")
end

"""
Task 5B: Create time series plots for 2D visualizations
"""
function create_time_series_plots(df, n, numeric_columns)
    # Initialize array to store individual plots
    plots = []
    # Define color palette for different plots
    colors = [:blue, :red, :green, :purple, :orange, :brown, :pink, :gray, :cyan]
    
    # Sort dates in reverse order and take first n entries
    sorted_dates = sort(df[1:n, :Date], rev=true)
    
    # TODO: Create time series plots for each numerical column
    for (col) in (numeric_columns)
        p = plot(sorted_dates, df[1:n, col],
                    title="Time Series of $(col)",
                    xlabel="Date", ylabel=col,
                    color=colors[findfirst(==(col), numeric_columns)],
                    legend=false)
            push!(plots, p)
    end

    # Combine all plots into a 3x3 grid
    final_plot = plot(plots..., layout=(3,3), size=(4800,4800))
    # Save the final visualization
    savefig(final_plot, "time-series-all-numericals.png")
end

# Main execution function
function main()
    # Load and prepare the dataset
    numeric_columns = ["SP500", "Dividend", "Earnings", "Consumer Price Index", "Long Interest Rate", "Real Dividend", "Real Earnings", "PE10" ]
    df = load_and_preprocess_data("sp_500_stock_price.csv", numeric_columns)
    first(df, 10)
    # Normalize all numerical columns
    normalize_numerical_columns!(df, numeric_columns)
    first(df, 10)
    # Process and add time-based features
    process_time_features!(df)
    first(df, 10)
    println(df)
    # Calculate various statistical measures
    yearly_stats, monthly_stats, quarterly_stats = calculate_statistics(df)
    # Create visualization plots
    create_visualizations(df)
    
    # Remove time-based columns to avoid redundancy in time series plots
    select!(df, Not([:Year, :Month, :Quarter]))
    # Create time series plots for the most recent 100 entries
    create_time_series_plots(df, 100, numeric_columns)
end

# Execute the main function
main()

# Summary
# The data that was provided was historical data on the S&P 500, Mostly data related to the price of the index 
# but also some information on dividend payouts, price earnings ratios and other information. From this data 
# we were able to look at and derive some averages and other yearly data to help us understand the trends of the index.
# This information could be used by investors to base their decision on historical information and could also be used to try and predict
# future movement based on these historical averages and trends.