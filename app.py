from src.logger import logging #custome logger import
def main():
    try:
        logging.info("Starting the main function")

        #Simulate some application steps
        logging.info("Step 1: Initializing application")
        x=5
        y=10

        logging.info(f"Step 2: Perfroming calculation with values x={x} and y={y}")

        result =x+y
        logging.info(f"Step 3: Calculation complete. Resullt: {result}")

        #simulate a warning condition
        if result > 10:
            logging.warning(f"Result {result} is greater than threshold (10)")
    except Exception as e:
        logging.error("An error occured in main function",exc_info=True) 


if __name__=="__main__":
    logging.info("="*50)
    logging.info("Application execution has started")
    logging.info("="*50)
          