# Import the libraries we will use here.
from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import Returns
from quantopian.pipeline.filters import Q1500US


def initialize(context):
    """
    Called once at the start of the program. Any one-time
    startup logic goes here.
    """
    # Make weekly trades (every 6 days and 23.5 hours)
    # Go to function open_positions() for opening the weeks oders.
    schedule_function(open_positions, date_rules.week_start(), time_rules.market_open())
    # Go to function close_positions() for closing the weeks orders.
    schedule_function(close_positions, date_rules.week_end(), time_rules.market_close(minutes=30))

    # Create and attach pipeline (list of stocks in a calculated filter).
    #   1st Input: Function to be called for creating stock list
    #   2nd Input: Name of list to be referenced elsewhere.
    attach_pipeline(make_pipeline(context),'stock_list_filtered_by_sectors')


def make_pipeline(context):
    """
    A function to build out filtered stock list by sectors.
    """
    # Filter for stocks in the Q1500US universe. For more detail, see this post:
    # https://www.quantopian.com/posts/the-q500us-and-q1500us
    universe = Q1500US()

    # Possible short version of a pipeline without filters
    # return Pipeline(  
    # screen = Tradeable500US)
    
    
def handle_data(context, data):
    """
    This is called once per minute of the program
    """
    # This will only include data that needs to be calculated every minute.
    # This function may not be used if there are no needed calculations every minute.


def open_positions(context, data):
    """
    Called by the intitalize() function once per week.
    All calculations and research should be finished within this function
    """
    order_target_percent(context.spy, 0.10)


def close_positions(context, data):
    """
    Called by the intitalize() function once per week
    All transactions should be closed within this function.
    """
    # Iterate over each security in portfolio and close out each position
    for security in context.portfolio.positions:
      order_target_percent(security, 0)


def record_vars(context, data):
    """
    Used to plot data
    """


def before_trading_start(context, data):
    """
    All calculations to be performed at the start of every market opening
    """

    #  TODO: Bring in list of stocks


    #  TODO: Determine each companies quarterly and yearly earnings. If quarterly
    #        earnings > yearly earnings than the company is gaining in sales.


    #  TODO: Determine companies growth rate percentage. Compare with
    #        all other companies.

    
    #  TODO: Determine companies ROE = Net Income / Shareholders' Equity


    #  TODO: Determine companies revenues and costs (this is the companies earnings)


    #  TODO: Use Morningstar Sector Code, under "Built-in Classifiers" section of
    #        API. Under that section, look at class "Sector" that groups assets
    #        within each sector.

    
