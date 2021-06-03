from __future__ import annotations


class CalculatedRatios:
    calculated_market: float
    calculated_auction: float

    def __init__(self, c_market=0, c_auction=0):
        self.calculated_market = c_market
        self.calculated_auction = c_auction


class Ratios:
    market_ration: int
    auction_ration: int

    @classmethod
    def json_load(cls, data: dict) -> Ratios:
        """
        Load data from json to ratios model

        :param data: ratios dictionary
        :return: Loaded data
        """
        ratios = cls()
        ratios.market_ration = data['marketRatio']
        ratios.auction_ration = data['auctionRatio']
        return ratios


class Schedule:
    years: dict[str, Ratios]
    default_marked_ratio: float
    default_auction_ratio: float

    @classmethod
    def json_load(cls, data: dict) -> Schedule:
        """
        Load data from json to schedule model

        :param data: schedule dictionary
        :return: Loaded data
        """
        schedule = cls()
        schedule.default_auction_ratio = data['defaultAuctionRatio']
        schedule.default_marked_ratio = data['defaultMarketRatio']
        schedule.years = {}
        for year, value in data['years'].items():
            schedule.years[year] = Ratios.json_load(value)
        return schedule


class SaleDetails:
    cost: float
    retail_sale_count: int
    auction_sale_count: int

    @classmethod
    def json_load(cls, data: dict) -> SaleDetails:
        """
        Load data from json to sale details model

        :param data: saleDetail dictionary
        :return: Loaded data
        """
        sd = cls()
        sd.cost = data['cost']
        sd.retail_sale_count = data['retailSaleCount']
        sd.auction_sale_count = data['auctionSaleCount']
        return sd


class Classification:
    category: str
    subcategory: str
    make: str
    model: str

    def __init__(self, **kwargs):
        self.category = kwargs['category']
        self.subcategory = kwargs['subcategory']
        self.make = kwargs['make']
        self.model = kwargs['model']


class EquipmentSet:
    id: str
    schedule: Schedule
    sale_details: SaleDetails
    classification: Classification

    @classmethod
    def json_load(cls, id: str, data: dict) -> EquipmentSet:
        """
        Load data from json to equipment set model

        :param id: The set ID, primary key in a database
        :param data: Contains more set info
        :return: Loaded data
        """
        es = cls()
        es.id = id
        es.schedule = Schedule.json_load(data['schedule'])
        es.sale_details = SaleDetails.json_load(data['saleDetails'])
        # classification has the same data structure, no need to create/use a json_load()
        es.classification = Classification(**data['classification'])
        return es
