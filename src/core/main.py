from pathlib import Path
from loguru import logger  # type: ignore
import click

# import logging
from common.io_operations import IOOperations  # type: ignore
from common.logging.loguru_setup import LoguruSetup  # type: ignore
from common.logging.logging_constants import LoggingConstants  # type: ignore
from core.helper.main_helper import MainHelper

logging_constants = LoggingConstants()
io_operations = IOOperations()
main_helper = MainHelper()


# @click.command()
# @click.option("-n", "--number_results", type=int, help="Number of threads to scrape")
# @click.option("-x", "--scrape", type=click.Choice(["user", "subreddits"]), default="hot",
#               help="Scrape user or subreddit")
# @click.option("-s", "--sorting_filter", type=click.Choice(["top", "hot", "new"]), default="hot", help="Filter threads")
# @click.option("-u", "--reddit_user", type=str, help="The reddit user to search")
# @click.option("-r", "--subreddits", type=str, help="The subreddit/s to search")
# @click.option("-d", "--details", is_flag=True, default=False,
#               help="If enable outputs the detailed list of threads of each subreddit provided into an individual file")
# @click.option("-o", "--output", type=str, help="The directory to output the downloads")
# @click.option("-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode")
# def main(number_results, scrape, sorting_filter, reddit_user, subreddits, details, output, verbose):
#     """
#     Script main entry point
#     """
#
#     # Setups directories used in the application
#     with logger.catch(reraise=True):
#         logger.remove()
#         output_directory = io_operations.init_directories(output)
#
#     logger.debug("[1] - STARTING reddit_scrapper")
#
#     # Setups logging for the application
#     LoguruSetup.script_logger_config_dict(
#         logger,
#         output_directory,
#         Path(logging_constants.log_filename).name,
#         logging_constants.default_log_stfout_level,
#         logging_constants.default_log_format,
#         logging_constants.default_log_colorizing,
#         logging_constants.default_log_rotation,
#         logging_constants.default_log_retention,
#         logging_constants.default_log_compression,
#         logging_constants.default_log_delay,
#         logging_constants.default_log_mode,
#         logging_constants.default_log_buffering,
#         logging_constants.default_log_encoding,
#         logging_constants.default_log_serialize,
#         logging_constants.default_log_backtrace,
#         logging_constants.default_log_diagnose,
#         logging_constants.default_log_enqueue,
#         logging_constants.default_log_catch,
#         False,  # enables/disables debug mode logs
#     )
#
#     # Scrapes a user or subreddit
#     match scrape:
#         case "user":
#             main_helper.scrape_user(
#                 reddit_user, sorting_filter, number_results, output_directory, verbose)
#
#         case "subreddits":
#             main_helper.scrape_subreddit(
#                 subreddits, sorting_filter, number_results, details, output_directory,  verbose)
#
#     logger.debug("[10] - ENDING reddit_scrapper")

main = click.Group(help="JSON tools")


@main.command("user", help="Scrape user threads")
@click.argument('reddit_user', type=str, nargs=-1)
#@click.option("-u", "--reddit_user", type=str, help="The reddit user to search")
@click.option("-n", "--number_results", type=int, help="Number of threads to scrape")
@click.option("-s", "--sorting_filter", type=click.Choice(["top", "hot", "new"]), default="hot", help="Filter threads")
@click.option("-o", "--output", type=str, help="The directory to output the downloads")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode")
def main_scrape_user(number_results, sorting_filter, reddit_user, output, verbose):
    # Setups directories used in the application
    with logger.catch(reraise=True):
        logger.remove()
        output_directory = io_operations.init_directories(output)

    # Setups logging for the application
    LoguruSetup.script_logger_config_dict(
        logger,
        output_directory,
        Path(logging_constants.log_filename).name,
        logging_constants.default_log_stfout_level,
        logging_constants.default_log_format,
        logging_constants.default_log_colorizing,
        logging_constants.default_log_rotation,
        logging_constants.default_log_retention,
        logging_constants.default_log_compression,
        logging_constants.default_log_delay,
        logging_constants.default_log_mode,
        logging_constants.default_log_buffering,
        logging_constants.default_log_encoding,
        logging_constants.default_log_serialize,
        logging_constants.default_log_backtrace,
        logging_constants.default_log_diagnose,
        logging_constants.default_log_enqueue,
        logging_constants.default_log_catch,
        False,  # enables/disables debug mode logs
    )

    main_helper.scrape_user(
        "".join(reddit_user) if len(reddit_user) > 0 else None,
        sorting_filter, number_results, output_directory, verbose)


@main.command("subreddits", help="Scrape subreddits threads")
#@click.option("-r", "--subreddits", type=str, help="The subreddit/s to search")
@click.argument('subreddits', type=str, nargs=-1)
@click.option("-n", "--number_results", type=int, help="Number of threads to scrape")
@click.option("-s", "--sorting_filter", type=click.Choice(["top", "hot", "new"]), default="hot", help="Filter threads")
@click.option("-d", "--details", is_flag=True, default=False,
              help="If enable outputs the detailed list of threads of each subreddit provided into an individual file")
@click.option("-o", "--output", type=str, help="The directory to output the downloads")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode")
def main_scrape_subreddits(number_results, sorting_filter, subreddits, details, output, verbose):
    # Setups directories used in the application
    with logger.catch(reraise=True):
        logger.remove()
        output_directory = io_operations.init_directories(output)


    # Setups logging for the application
    LoguruSetup.script_logger_config_dict(
        logger,
        output_directory,
        Path(logging_constants.log_filename).name,
        logging_constants.default_log_stfout_level,
        logging_constants.default_log_format,
        logging_constants.default_log_colorizing,
        logging_constants.default_log_rotation,
        logging_constants.default_log_retention,
        logging_constants.default_log_compression,
        logging_constants.default_log_delay,
        logging_constants.default_log_mode,
        logging_constants.default_log_buffering,
        logging_constants.default_log_encoding,
        logging_constants.default_log_serialize,
        logging_constants.default_log_backtrace,
        logging_constants.default_log_diagnose,
        logging_constants.default_log_enqueue,
        logging_constants.default_log_catch,
        False,  # enables/disables debug mode logs
    )

    main_helper.scrape_subreddit(
        ", ".join(subreddits) if len(subreddits) > 0 else None
        , sorting_filter, number_results, details, output_directory, verbose)


if __name__ == "__main__":
    exit(main())  # pylint: disable=no-value-for-parameter
