# Quantopian_Jwes
Algorithm for financial programming

REFRENCED FUNCTIONS:
   Three Types of functions called to handle data during trading.
	- initialize():  is to perform any one-time starup logic called when the program starts.
	   - Takes one arguement: intialize(context)
	- handle_data(): is to decide what orders, if any, should be placed each minute of simulation and live-trading.
	   - Takes two input arguments: handle_data(context, data)
	- before_trading_start(): is called once per day before the market opens. Used when selecting securities to order.
	   - Takes two input arguments: before_trading_start(context, data)
   ALL global variables shall be initialized in the initialize() function and must use 'context'.
	- context: is always used before every variable set, such as, 'context.message' = 'hello'.
   Selecting a specific stock may be done by refrencing the security id associated with it.
	- sid(): is a function quantopian uses to grab that specific stock.
	   - Takes one input argument: sid(security_id selected). Example to get apple stock would be 
             'context.aapl = sid(24)', as '24' is Apple's security id.
   Ordering Securities.
	- order_target_percent(): allows us to to order securities to a target percent of our portfolio.
           - To order 50% of Apple stock: order_target_percent(sid(24), .50).
   The "data" Object used to loop up current or historical pricing and volume data from any security.
	- data.current(): is used to retrieve the most recent value of given field for a given value.
	   - Takes two arguments: data.current(sid(24), 'price'), or it can be a list as
             data.current([sid(24), sid(8554)], ['low', 'high'])
	- data.can_trade(): returns "True" if we are allowed to place on order on that asset.
	   - Takes one argument: data.can_trade(sid(24))
	- data.history(): allows us to analyze an asset.
	   - Takes four arguments: 
		hist = data.history(sid(24), 'price' 10, '1d')
	   	mean_ price = hist.mean()