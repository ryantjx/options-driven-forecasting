# Financial Data Column Definitions

## Basic Market Data
- **timestamp**: The date and time at which the data was recorded
- **open**: The opening price of the asset for the given time period
- **returns_log_lag1**: Logarithmic returns with a lag of 1 period (log of current price divided by previous price)
- **volume**: Trading volume of the asset during the time period

## Perpetual Futures Data
<!-- - **perpetual_price**: Current price of the perpetual futures contract -->
<!-- - **perpetual_index**: Value of the index that the perpetual contract tracks -->
- **perpetual_basis**: Difference between perpetual futures price and the spot index (perpetual_price - perpetual_index)
- **perpetual_funding**: Current funding rate for the perpetual contract
- **perpetual_yield**: Annualized yield implied by the perpetual contract
- **perpetual_volume**: Trading volume for the perpetual contract
<!-- - **perpetual_volume_coin**: Trading volume for the perpetual contract expressed in coins/tokens -->
- **perpetual_oi**: Open interest for the perpetual contract (in USD)
<!-- - **perpetual_oi_coin**: Open interest for the perpetual contract expressed in coins/tokens -->
<!-- - **perpetual_oi_volume24h**: Ratio of open interest to 24-hour volume for the perpetual contract -->
- **perpetual_long_short_ratio**: Ratio of long positions to short positions in the perpetual contract
<!-- - **perpetual_next_funding**: Predicted next funding rate for the perpetual contract -->
<!-- - **perpetual_ask**: Lowest ask price for the perpetual contract
- **perpetual_bid**: Highest bid price for the perpetual contract -->
<!-- - **perpetual_ask_amount**: Amount available at the lowest ask price -->
<!-- - **perpetual_bid_amount**: Amount available at the highest bid price -->

## Realized Volatility Metrics
- **rv_3d**: Realized volatility calculated over a 3-day period
- **rv_7d**: Realized volatility calculated over a 7-day period
- **rv_30d**: Realized volatility calculated over a 30-day period
- **rv_60d**: Realized volatility calculated over a 60-day period
- **rv_90d**: Realized volatility calculated over a 90-day period
- **rv_180d**: Realized volatility calculated over a 180-day period
- **rv_270d**: Realized volatility calculated over a 270-day period
- **rv_365d**: Realized volatility calculated over a 365-day period

## At-the-Money Implied Volatility (ATMIV)
- **atmiv_1d**: At-the-money implied volatility for 1-day options
- **atmiv_7d**: At-the-money implied volatility for 7-day options
- **atmiv_14d**: At-the-money implied volatility for 14-day options
- **atmiv_30d**: At-the-money implied volatility for 30-day options
- **atmiv_60d**: At-the-money implied volatility for 60-day options
- **atmiv_90d**: At-the-money implied volatility for 90-day options
- **atmiv_180d**: At-the-money implied volatility for 180-day options
- **atmiv_365d**: At-the-money implied volatility for 365-day options


## Volatility and Greeks Metrics
- **dvol**: Dynamic volatility index
<!-- - **index_x**, **index_y**: Index values (possibly from different sources or calculations) -->
- **gex**: Gamma exposure (measures the amount of gamma in the market)
- **vex**: Vega exposure (measures sensitivity to volatility changes)
- **gex_plus**: Positive gamma exposure
<!-- - **index_price**: Price of the underlying index -->

## Open Interest Put-Call Metrics
- **oi_pcratio**: Put-call ratio based on open interest
- **oi_put**: Open interest for put options
- **oi_call**: Open interest for call options
- **oi_premium_pcratio**: Put-call ratio based on premium open interest
- **oi_premium_put**: Premium open interest for put options
- **oi_premium_call**: Premium open interest for call options
- **oi_put_notional**: Notional value of put option open interest
- **oi_call_notional**: Notional value of call option open interest

<!-- - **total_oi**: Total open interest (puts + calls)
- **total_oi_premium**: Total premium open interest
- **total_oi_notional**: Total notional value of open interest -->

## Volume-Based Put-Call Metrics
- **volume_pcratio**: Put-call ratio based on trading volume
- **volume_put**: Trading volume for put options
- **volume_call**: Trading volume for call options
- **volume_premium_ratio**: Put-call ratio based on premium volume
- **volume_premium_put**: Premium volume for put options
- **volume_premium_call**: Premium volume for call options
- **volume_put_notional**: Notional value of put option volume
- **volume_call_notional**: Notional value of call option volume
- **volume_premium**: Total premium volume
- **volume_volume**: Total trading volume
- **volume_notional**: Total notional value of volume

## Butterfly Spreads
- **butterfly10D_1d**: 10-delta butterfly spread for 1-day options
- **butterfly10D_7d**: 10-delta butterfly spread for 7-day options
- **butterfly10D_14d**: 10-delta butterfly spread for 14-day options
- **butterfly10D_30d**: 10-delta butterfly spread for 30-day options
- **butterfly10D_60d**: 10-delta butterfly spread for 60-day options
- **butterfly10D_90d**: 10-delta butterfly spread for 90-day options
- **butterfly10D_180d**: 10-delta butterfly spread for 180-day options
- **butterfly10D_365d**: 10-delta butterfly spread for 365-day options
- **butterfly25D_1d**: 25-delta butterfly spread for 1-day options
- **butterfly25D_7d**: 25-delta butterfly spread for 7-day options
- **butterfly25D_14d**: 25-delta butterfly spread for 14-day options
- **butterfly25D_30d**: 25-delta butterfly spread for 30-day options
- **butterfly25D_60d**: 25-delta butterfly spread for 60-day options
- **butterfly25D_90d**: 25-delta butterfly spread for 90-day options
- **butterfly25D_180d**: 25-delta butterfly spread for 180-day options
- **butterfly25D_365d**: 25-delta butterfly spread for 365-day options

## Gamma Bands
- **gammaband1D_upper_1_4**: 1-day upper gamma band at 1/4 level
- **gammaband1D_upper_1_2**: 1-day upper gamma band at 1/2 level
- **gammaband1D_upper_1**: 1-day upper gamma band at 1 level
- **gammaband1D_upper_2**: 1-day upper gamma band at 2 level
- **gammaband1D_lower_1_4**: 1-day lower gamma band at 1/4 level
- **gammaband1D_lower_1_2**: 1-day lower gamma band at 1/2 level
- **gammaband1D_lower_1**: 1-day lower gamma band at 1 level
- **gammaband1D_lower_2**: 1-day lower gamma band at 2 level
- **gammaband30D_upper_1_4**: 30-day upper gamma band at 1/4 level
- **gammaband30D_upper_1_2**: 30-day upper gamma band at 1/2 level
- **gammaband30D_upper_1**: 30-day upper gamma band at 1 level
- **gammaband30D_upper_2**: 30-day upper gamma band at 2 level
- **gammaband30D_lower_1_4**: 30-day lower gamma band at 1/4 level
- **gammaband30D_lower_1_2**: 30-day lower gamma band at 1/2 level
- **gammaband30D_lower_1**: 30-day lower gamma band at 1 level
- **gammaband30D_lower_2**: 30-day lower gamma band at 2 level
- **gammaband7D_upper_1_4**: 7-day upper gamma band at 1/4 level
- **gammaband7D_upper_1_2**: 7-day upper gamma band at 1/2 level
- **gammaband7D_upper_1**: 7-day upper gamma band at 1 level
- **gammaband7D_upper_2**: 7-day upper gamma band at 2 level
- **gammaband7D_lower_1_4**: 7-day lower gamma band at 1/4 level
- **gammaband7D_lower_1_2**: 7-day lower gamma band at 1/2 level
- **gammaband7D_lower_1**: 7-day lower gamma band at 1 level
- **gammaband7D_lower_2**: 7-day lower gamma band at 2 level

## Risk Reversal
- **riskreversal10D_1d**: 10-delta risk reversal for 1-day options
- **riskreversal10D_7d**: 10-delta risk reversal for 7-day options
- **riskreversal10D_14d**: 10-delta risk reversal for 14-day options
- **riskreversal10D_30d**: 10-delta risk reversal for 30-day options
- **riskreversal10D_60d**: 10-delta risk reversal for 60-day options
- **riskreversal10D_90d**: 10-delta risk reversal for 90-day options
- **riskreversal10D_180d**: 10-delta risk reversal for 180-day options
- **riskreversal10D_365d**: 10-delta risk reversal for 365-day options
- **riskreversal25D_1d**: 25-delta risk reversal for 1-day options
- **riskreversal25D_7d**: 25-delta risk reversal for 7-day options
- **riskreversal25D_14d**: 25-delta risk reversal for 14-day options
- **riskreversal25D_30d**: 25-delta risk reversal for 30-day options
- **riskreversal25D_60d**: 25-delta risk reversal for 60-day options
- **riskreversal25D_90d**: 25-delta risk reversal for 90-day options
- **riskreversal25D_180d**: 25-delta risk reversal for 180-day options
- **riskreversal25D_365d**: 25-delta risk reversal for 365-day options

## Volatility Skew
- **skew10D_1d**: 10-delta volatility skew for 1-day options
- **skew10D_7d**: 10-delta volatility skew for 7-day options
- **skew10D_14d**: 10-delta volatility skew for 14-day options
- **skew10D_30d**: 10-delta volatility skew for 30-day options
- **skew10D_60d**: 10-delta volatility skew for 60-day options
- **skew10D_90d**: 10-delta volatility skew for 90-day options
- **skew10D_180d**: 10-delta volatility skew for 180-day options
- **skew10D_365d**: 10-delta volatility skew for 365-day options
- **skew25D_1d**: 25-delta volatility skew for 1-day options
- **skew25D_7d**: 25-delta volatility skew for 7-day options
- **skew25D_14d**: 25-delta volatility skew for 14-day options
- **skew25D_30d**: 25-delta volatility skew for 30-day options
- **skew25D_60d**: 25-delta volatility skew for 60-day options
- **skew25D_90d**: 25-delta volatility skew for 90-day options
- **skew25D_180d**: 25-delta volatility skew for 180-day options
- **skew25D_365d**: 25-delta volatility skew for 365-day options

## Volatility Index
- **vix_15d**: Volatility index for 15-day period
- **vix_30d**: Volatility index for 30-day period
- **vix_60d**: Volatility index for 60-day period
- **vix_90d**: Volatility index for 90-day period
- **vix_180d**: Volatility index for 180-day period

