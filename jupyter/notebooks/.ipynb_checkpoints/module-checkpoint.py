

def mongodbdata(file_path, sheet_name, host_path, db_name, collection_name):
    """
    - mongodbdata function loads data from xlsx file  
    - It creates and returns the data as a pandas dataframe
    - It creates a database inside mongodb 
    - It injects the data as collection inside the database
    """
    
    # Checking if the file extension is '.xlsx'
    if not file_path.endswith('.xlsx'):
        raise TypeError('the file format or extension is not valid xlsx')
    # Read an Excel file into a pandas DataFrame
    df = pd.read_excel(io=file_path, sheet_name=sheet_name)
    
    # Connect to MongoDB
    client = MongoClient(host_path)
    # Create database db_name
    db = client[db_name]
    # drop collection collection_name if exists 
    db[collection_name].drop()
    # Create collection collection_name
    collection = db[collection_name]
    # Insert collection
    collection.insert_many(df.to_dict("records"))
    # Checking if The collection was successfully created
    try:
        client[db_name].validate_collection(collection_name)  # Try to validate a collection
        print(f"The collection {collection_name} is successfully created")
    except pymongo.errors.OperationFailure:  # If the collection doesn't exist
        print(f"The collection {collection_name} is not yet created")
        
    return df
