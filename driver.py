from modules.processors.gdelt.gdelt_processor import GDELTProcessor
from modules.processors.gdelt.daily_gdelt_processor import GDELTDailyProcessor
from modules.processors.gdelt.monthly_gdelt_processor import GDELTMonthlyProcessor
from modules.processors.gdelt.yearly_gdelt_processor import GDELTYearlyProcessor


gdelt_processor = GDELTProcessor()

'''
gdelt_processor.process(GDELTDailyProcessor(start_event_date=20170501,
                                             end_event_date=20170531))


gdelt_processor.process(GDELTMonthlyProcessor(
    start_event_month=201204,
    end_event_month=201212))
    '''

gdelt_processor.process(GDELTYearlyProcessor(
    start_event_year=1979,
    end_event_year=2012))


