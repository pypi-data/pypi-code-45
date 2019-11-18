import lusid
import pandas as pd
from lusidtools import cocoon
from lusidtools.cocoon.utilities import checkargs
from lusidtools.cocoon.validator import Validator
from lusidtools.cocoon.async_tools import run_in_executor
import asyncio
from lusidtools.cocoon.dateorcutlabel import DateOrCutLabel
import logging


class BatchLoader:
    """
    This class contains all the methods used for loading data in batches. The @run_in_executor decorator makes the
    synchronous functions awaitable
    """

    @staticmethod
    @run_in_executor
    def load_instrument_batch(
        api_factory: lusid.utilities.ApiClientFactory, instrument_batch: list, **kwargs
    ) -> lusid.models.UpsertInstrumentsResponse:
        """
        Upserts a batch of instruments to LUSID

        :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
        :param list[lusid.models.InstrumentDefinition] instrument_batch: The batch of instruments to upsert

        :return: UpsertInstrumentsResponse: The response from LUSID
        """

        # Ensure that the list of allowed unique identifiers exists
        if "unique_identifiers" not in list(kwargs.keys()):
            unique_identifiers = cocoon.instruments.get_unique_identifiers(
                api_factory=api_factory
            )
        else:
            unique_identifiers = kwargs["unique_identifiers"]

        @checkargs
        def get_alphabetically_first_identifier_key(
            instrument: lusid.models.InstrumentDefinition, unique_identifiers: list
        ):
            """
            Gets the alphabetically first occurring unique identifier on an instrument and use it as the correlation
            id on the request

            :param lusid.models.InstrumentDefinition instrument: The instrument to create a correlation id for
            :param list[str] unique_identifiers: The list of allowed unique identifiers

            :return: str: The correlation id to use on the request
            """
            unique_identifiers_populated = list(
                set(unique_identifiers).intersection(
                    set(list(instrument.identifiers.keys()))
                )
            )
            unique_identifiers_populated.sort()
            first_unique_identifier_alphabetically = unique_identifiers_populated[0]
            return f"{first_unique_identifier_alphabetically}: {instrument.identifiers[first_unique_identifier_alphabetically].value}"

        return api_factory.build(lusid.api.InstrumentsApi).upsert_instruments(
            instruments={
                get_alphabetically_first_identifier_key(
                    instrument, unique_identifiers
                ): instrument
                for instrument in instrument_batch
            }
        )

    @staticmethod
    @run_in_executor
    def load_quote_batch(
        api_factory: lusid.utilities.ApiClientFactory, quote_batch: list, **kwargs
    ) -> lusid.models.UpsertQuotesResponse:
        """
        Upserts a batch of quotes into LUSID

        :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
        :param list[lusid.models.UpsertQuoteRequest] quote_batch: The batch of quotes to upsert
        :param str scope: The scope to upsert the quotes into

        :return: lusid.models.UpsertQuotesResponse: The response from LUSID
        """

        if "scope" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load quotes without a scope, please ensure that a scope is provided."
            )

        return api_factory.build(lusid.api.QuotesApi).upsert_quotes(
            scope=kwargs["scope"],
            quotes={
                "_".join(
                    [
                        quote.quote_id.quote_series_id.instrument_id,
                        quote.quote_id.quote_series_id.instrument_id_type,
                        str(quote.quote_id.effective_at),
                    ]
                ): quote
                for quote in quote_batch
            },
        )

    @staticmethod
    @run_in_executor
    def load_transaction_batch(
        api_factory: lusid.utilities.ApiClientFactory, transaction_batch: list, **kwargs
    ) -> lusid.models.UpsertPortfolioTransactionsResponse:
        """
        Upserts a batch of transactions into LUSID

        :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
        :param str scope: The scope of the Transaction Portfolio to upsert the transactions into
        :param str code: The code of the Transaction Portfolio, together with the scope this uniquely identifies the portfolio
        :param list[lusid.models.TransactionRequest] transaction_batch: The batch of transactions to upsert

        :return: lusid.models.UpsertPortfolioTransactionsResponse: The response from LUSID
        """

        if "scope" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load transactions without a scope, please ensure that a scope is provided."
            )

        if "code" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load transactions without a portfolio code, please ensure that a code is provided."
            )

        return api_factory.build(
            lusid.api.TransactionPortfoliosApi
        ).upsert_transactions(
            scope=kwargs["scope"], code=kwargs["code"], transactions=transaction_batch
        )

    @staticmethod
    @run_in_executor
    def load_holding_batch(
        api_factory: lusid.utilities.ApiClientFactory, holding_batch: list, **kwargs
    ) -> lusid.models.HoldingsAdjustment:
        """
        Upserts a batch of holdings into LUSID

        :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
        :param list[lusid.models.AdjustHoldingRequest] holding_batch: The batch of holdings
        :param kwargs: 'scope', 'code', 'effective_at' The parameters required for the API call

        :return: lusid.models.HoldingsAdjustment: The response from LUSID
        """

        if "scope" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load transactions without a scope, please ensure that a scope is provided."
            )

        if "code" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load transactions without a portfolio code, please ensure that a code is provided."
            )

        if "effective_at" not in list(kwargs.keys()):
            raise KeyError(
                """There is no mapping for effective_at in the required mapping, please add it"""
            )

        return api_factory.build(lusid.api.TransactionPortfoliosApi).set_holdings(
            scope=kwargs["scope"],
            code=kwargs["code"],
            effective_at=str(DateOrCutLabel(kwargs["effective_at"])),
            holding_adjustments=holding_batch,
        )

    @staticmethod
    @run_in_executor
    def load_portfolio_batch(
        api_factory: lusid.utilities.ApiClientFactory, portfolio_batch: list, **kwargs
    ) -> lusid.models.Portfolio:
        """
        Upserts a batch of portfolios to LUSID

        :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
        :param list[lusid.models.CreateTransactionPortfolioRequest] portfolio_batch: The batch of portfolios to create
        :param kwargs: 'scope', 'code' arguments required for the API call

        :return: lusid.models.Portfolio: The response from LUSID
        """

        if "scope" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load transactions without a scope, please ensure that a scope is provided."
            )

        if "code" not in list(kwargs.keys()):
            raise KeyError(
                "You are trying to load transactions without a portfolio code, please ensure that a code is provided."
            )

        try:
            return api_factory.build(lusid.api.PortfoliosApi).get_portfolio(
                scope=kwargs["scope"], code=kwargs["code"]
            )
        except lusid.exceptions.ApiException as e:
            if e.status == 404:
                return api_factory.build(
                    lusid.api.TransactionPortfoliosApi
                ).create_portfolio(
                    scope=kwargs["scope"], transaction_portfolio=portfolio_batch[0]
                )
            # Add in here upsert portfolio properties if it does exist


async def load_data(
    api_factory: lusid.utilities.ApiClientFactory,
    data_frame: pd.DataFrame,
    mapping_required: dict,
    mapping_optional: dict,
    property_columns: list,
    properties_scope: str,
    instrument_identifier_mapping: dict,
    file_type: str,
    domain_lookup: dict,
    **kwargs,
):
    """
    This function populates the required models from a DataFrame and loads the data into LUSID

    :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
    :param pd.DataFrame data_frame: The DataFrame containing the data to load
    :param dict mapping_required: The required mapping
    :param dict mapping_optional: The optional mapping
    :param list property_columns: The property columns to add as property values
    :param str properties_scope: The scope to add the property values in
    :param dict instrument_identifier_mapping: The mapping for the identifiers
    :param int batch_size: The batch size to use
    :param str file_type: The file type to load
    :param dict domain_lookup: The domain lookup
    :param kwargs: Arguments specific to each call e.g. effective_at for holdings

    :return: BatchLoader StaticMethod: A static method on BatchLoader
    """

    # Get the top level model used for this request e.g. lusid.models.InstrumentDefintion for upsert instruments
    top_level_model = getattr(lusid.models, domain_lookup[file_type]["top_level_model"])

    # Verify that all the required attributes for this top level model exist in the provided required mapping
    cocoon.utilities.verify_all_required_attributes_mapped(
        swagger_dict=cocoon.utilities.get_swagger_dict(
            api_url=api_factory.api_client.configuration.host
        ),
        mapping=mapping_required,
        model_object=top_level_model,
        exempt_attributes=["identifiers", "properties", "instrument_identifiers"],
    )

    # Get the data types of the columns to be added as properties
    property_dtypes = data_frame.loc[:, property_columns].dtypes

    unique_identifiers = kwargs["unique_identifiers"]

    # Iterate over the DataFrame creating the single requests
    single_requests = []
    for index, row in data_frame.iterrows():

        # Create the property values for this row
        if domain_lookup[file_type]["domain"] is None:
            properties = None
        else:
            properties = cocoon.properties.create_property_values(
                row=row,
                scope=properties_scope,
                domain=domain_lookup[file_type]["domain"],
                dtypes=property_dtypes,
            )

        # Create identifiers for this row if applicable
        # If no instrument identifier mapping is provided return None as no identifiers are required
        if instrument_identifier_mapping is None or not bool(
            instrument_identifier_mapping
        ):
            identifiers = None
        else:
            identifiers = cocoon.instruments.create_identifiers(
                index=index,
                row=row,
                file_type=file_type,
                instrument_identifier_mapping=instrument_identifier_mapping,
                unique_identifiers=unique_identifiers,
                full_key_format=kwargs["full_key_format"],
            )

        # Construct the from the mapping, properties and identifiers the single request object and add it to the list
        single_requests.append(
            cocoon.utilities.populate_model(
                model_object=top_level_model,
                required_mapping=mapping_required,
                optional_mapping=mapping_optional,
                row=row,
                properties=properties,
                identifiers=identifiers,
            )
        )

    # Dynamically call the correct async function to use based on the file type
    return await getattr(BatchLoader, f"load_{file_type}_batch")(
        api_factory,
        single_requests,
        # Any specific arguments e.g. 'code' for transactions, 'effective_at' for holdings is passed in via **kwargs
        **kwargs,
    )


async def construct_batches(
    api_factory: lusid.utilities.ApiClientFactory,
    data_frame: pd.DataFrame,
    mapping_required: dict,
    mapping_optional: dict,
    property_columns: list,
    properties_scope: str,
    instrument_identifier_mapping: dict,
    batch_size: int,
    file_type: str,
    domain_lookup: dict,
    **kwargs,
):

    """
    This constructs the batches and asynchronously sends them to be loaded into LUSID

    :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
    :param pd.DataFrame data_frame: The DataFrame containing the data to load
    :param dict mapping_required: The required mapping
    :param dict mapping_optional: The optional mapping
    :param list property_columns: The property columns to add as property values
    :param str properties_scope: The scope to add the property values in
    :param dict instrument_identifier_mapping: The mapping for the identifiers
    :param int batch_size: The batch size to use
    :param str file_type: The file type to load
    :param dict domain_lookup: The domain lookup
    :param kwargs: Arguments specific to each call e.g. effective_at for holdings

    :return: dict: Contains the success responses and the errors (where an API exception has been raised)
    """

    # Get the different behaviours required for different entities e.g quotes can be batched without worrying about portfolios
    batching_no_portfolios = [
        file_type
        for file_type, settings in domain_lookup.items()
        if not settings["portfolio_specific"]
    ]
    batching_with_portfolios = [
        file_type
        for file_type, settings in domain_lookup.items()
        if settings["portfolio_specific"]
    ]

    if file_type in batching_no_portfolios:

        async_batches = [
            data_frame.iloc[i : i + batch_size]
            for i in range(0, len(data_frame), batch_size)
        ]

        sync_batches = [
            {
                "async_batches": async_batches,
                "codes": [None] * len(async_batches),
                "effective_at": [None] * len(async_batches),
            }
        ]

    elif file_type in batching_with_portfolios:

        if "effective_at" in domain_lookup[file_type]["required_call_attributes"]:

            unique_effective_dates = list(
                data_frame[mapping_required["effective_at"]].unique()
            )

            effective_at_groups = [
                data_frame.loc[
                    data_frame[mapping_required["effective_at"]] == effective_at
                ]
                for effective_at in unique_effective_dates
            ]

            sync_batches = [
                {
                    "async_batches": [
                        data_frame.loc[data_frame[mapping_required["code"]] == code]
                        for code in list(
                            effective_at_group[mapping_required["code"]].unique()
                        )
                    ],
                    "codes": list(
                        effective_at_group[mapping_required["code"]].unique()
                    ),
                    "effective_at": [
                        list(
                            effective_at_group[
                                mapping_required["effective_at"]
                            ].unique()
                        )[0]
                    ]
                    * len(list(effective_at_group[mapping_required["code"]].unique())),
                }
                for effective_at_group in effective_at_groups
            ]

        else:

            unique_portfolios = list(data_frame[mapping_required["code"]].unique())

            async_batches = [
                data_frame.loc[data_frame[mapping_required["code"]] == code]
                for code in unique_portfolios
            ]

            sync_batches = [
                {
                    "async_batches": async_batches,
                    "codes": [str(code) for code in unique_portfolios],
                    "effective_at": [None] * len(async_batches),
                }
            ]

    # Asynchronously load the data into LUSID
    responses = [
        await asyncio.gather(
            *[
                load_data(
                    api_factory=api_factory,
                    data_frame=async_batch,
                    mapping_required=mapping_required,
                    mapping_optional=mapping_optional,
                    property_columns=property_columns,
                    properties_scope=properties_scope,
                    instrument_identifier_mapping=instrument_identifier_mapping,
                    file_type=file_type,
                    domain_lookup=domain_lookup,
                    code=code,
                    effective_at=effective_at,
                    **kwargs,
                )
                for async_batch, code, effective_at in zip(
                    sync_batch["async_batches"],
                    sync_batch["codes"],
                    sync_batch["effective_at"],
                )
            ],
            return_exceptions=True,
        )
        for sync_batch in sync_batches
    ]

    responses_flattened = [
        response for responses_sub in responses for response in responses_sub
    ]

    # Raise any internal exceptions rather than propagating them to the response
    for response in responses_flattened:
        if isinstance(response, Exception) and not isinstance(
            response, lusid.exceptions.ApiException
        ):
            raise response

    # Collects the exceptions as failures and successful calls as values
    return {
        "errors": [r for r in responses_flattened if isinstance(r, Exception)],
        "success": [r for r in responses_flattened if not isinstance(r, Exception)],
    }


@checkargs
def load_from_data_frame(
    api_factory: lusid.utilities.ApiClientFactory,
    scope: str,
    data_frame: pd.DataFrame,
    mapping_required: dict,
    mapping_optional: dict,
    file_type: str,
    identifier_mapping: dict = None,
    property_columns: list = None,
    properties_scope: str = None,
    batch_size: int = None,
    instrument_name_enrichment: bool = False,
):
    """
    Handles loading data from a DataFrame into LUSID

    :param lusid.utilities.ApiClientFactory api_factory: The api factory to use
    :param str scope: The scope of the resource to load the data into
    :param Pandas DataFrame data_frame: The DataFrame containing the data
    :param dict{str, str} mapping_required: The dictionary mapping the DataFrame columns to LUSID's required attributes
    :param dict{str, str} mapping_optional: The dictionary mapping the DataFrame columns to LUSID's optional attributes
    :param str file_type: The type of file e.g. transctions, instruments, holdings, quotes, portfolios
    :param dict{str, str} identifier_mapping: The dictionary mapping of LUSID instrument identifiers to identifiers in the DataFrame
    :param list[str] property_columns: The columns to create properties for
    :param str properties_scope: The scope to add the properties to
    :param int batch_size: The size of the batch to use when using upsert calls e.g. upsert instruments, upsert quotes etc.

    :return: dict responses: The responses from loading the data into LUSID
    """

    # A mapping between the file type and relevant attributes e.g. domain, top_level_model etc.
    domain_lookup = cocoon.utilities.load_json_file("config/domain_settings.json")

    # Convert the file type to lower case & singular as well as checking it is of the allowed value
    file_type = (
        Validator(file_type, "file_type")
        .make_singular()
        .make_lower()
        .check_allowed_value(list(domain_lookup.keys()))
        .value
    )

    # Set defaults aligned with the data type of each argument, this allows for users to provide None
    identifier_mapping = (
        Validator(identifier_mapping, "identifier_mapping")
        .set_default_value_if_none(default={})
        .discard_dict_keys_none_value()
        .value
    )

    properties_scope = (
        Validator(properties_scope, "properties_scope")
        .set_default_value_if_none(default=scope)
        .value
    )

    property_columns = (
        Validator(property_columns, "property_columns")
        .set_default_value_if_none(default=[])
        .value
    )

    batch_size = (
        Validator(batch_size, "batch_size")
        .set_default_value_if_none(domain_lookup[file_type]["default_batch_size"])
        .override_value(
            not domain_lookup[file_type]["batch_allowed"],
            domain_lookup[file_type]["default_batch_size"],
        )
        .value
    )

    # Discard mappings where the provided value is None
    mapping_required = (
        Validator(mapping_required, "mapping_required")
        .discard_dict_keys_none_value()
        .value
    )

    mapping_optional = (
        Validator(mapping_optional, "mapping_optional")
        .discard_dict_keys_none_value()
        .value
    )

    if instrument_name_enrichment:

        loop = cocoon.async_tools.start_event_loop_new_thread()

        data_frame, mapping_required = asyncio.run_coroutine_threadsafe(
            cocoon.instruments.enrich_instruments(
                api_factory=api_factory,
                data_frame=data_frame,
                instrument_identifier_mapping=identifier_mapping,
                mapping_required=mapping_required,
                constant_prefix="$",
            ),
            loop,
        ).result()

        # Stop the additional event loop
        loop.stop()

    """
    Unnest and populate defaults where a mapping is provided with column and/or default fields in a nested dictionary
    
    e.g.
    {'name': {
        'column': 'instrument_name',
        'default': 'unknown_name'
        }
    }
    
    rather than simply
    {'name': 'instrument_name'}
    """
    (
        data_frame,
        mapping_required,
    ) = cocoon.utilities.handle_nested_default_and_column_mapping(
        data_frame=data_frame, mapping=mapping_required, constant_prefix="$"
    )
    (
        data_frame,
        mapping_optional,
    ) = cocoon.utilities.handle_nested_default_and_column_mapping(
        data_frame=data_frame, mapping=mapping_optional, constant_prefix="$"
    )

    # Get all the DataFrame columns as well as those that contain at least one null value
    data_frame_columns = list(data_frame.columns.values)
    nan_columns = [
        column for column in data_frame_columns if data_frame[column].isna().any()
    ]

    # Validate that none of the provided columns are missing or invalid
    Validator(
        mapping_required, "mapping_required"
    ).get_dict_values().filter_list_using_first_character("$").check_subset_of_list(
        data_frame_columns, "DataFrame Columns"
    ).check_no_intersection_with_list(
        nan_columns, "Columns with Missing Values"
    )

    Validator(
        mapping_optional, "mapping_optional"
    ).get_dict_values().filter_list_using_first_character("$").check_subset_of_list(
        data_frame_columns, "DataFrame Columns"
    )

    Validator(
        identifier_mapping, "identifier_mapping"
    ).get_dict_values().filter_list_using_first_character("$").check_subset_of_list(
        data_frame_columns, "DataFrame Columns"
    )

    Validator(property_columns, "property_columns").check_subset_of_list(
        data_frame_columns, "DataFrame Columns"
    )

    # Converts higher level data types such as dictionaries and lists to strings
    data_frame = data_frame.applymap(cocoon.utilities.convert_cell_value_to_string)

    # Check for and create missing property defintions
    data_frame = cocoon.properties.create_missing_property_definitions_from_file(
        api_factory=api_factory,
        properties_scope=properties_scope,
        file_type=file_type,
        data_frame=data_frame,
        property_columns=property_columns,
        domain_lookup=domain_lookup,
    )

    # Start a new event loop in a new thread, this is required to run inside a Jupyter notebook
    loop = cocoon.async_tools.start_event_loop_new_thread()

    # Keyword arguments to be used in requests to the LUSID API
    keyword_arguments = {
        "scope": scope,
        # This handles that identifiers need to be specified differently based on the request type, allowing users
        # to provide either the entire key e.g. "Instrument/default/Figi" or just the code "Figi" for any request
        "full_key_format": domain_lookup[file_type]["full_key_format"],
        # Gets the allowed unique identifiers
        "unique_identifiers": cocoon.instruments.get_unique_identifiers(
            api_factory=api_factory
        ),
    }

    # Get the responses from LUSID
    responses = asyncio.run_coroutine_threadsafe(
        construct_batches(
            api_factory=api_factory,
            data_frame=data_frame,
            mapping_required=mapping_required,
            mapping_optional=mapping_optional,
            property_columns=property_columns,
            properties_scope=properties_scope,
            instrument_identifier_mapping=identifier_mapping,
            batch_size=batch_size,
            file_type=file_type,
            domain_lookup=domain_lookup,
            **keyword_arguments,
        ),
        loop,
    ).result()

    # Stop the additional event loop
    loop.stop()

    # Prefix the responses with the file type
    return {file_type + "s": responses}
