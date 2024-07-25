from fastapi import FastAPI

app=FastAPI()
# just for pratice
# @app.get("/hello/{name}")
# async def hello(name):
#     return f"hello world my name is {name}"

# to run this write
# uvicorn fast(filename):app(decorator) --reload

# reload do live update itself automatically we change in code

indian_places ={
'delhi': ['Red Fort', 'Qutub Minar', 'India Gate'],
'mumbai': ['Gateway of India', 'Marine Drive', 'ElephantaCaves'],
'jaipur': ['Hawa Mahal', 'Amber Fort', 'City Palace'],
'varanasi': ['Kashi Vishwanath Temple', 'Ghats of Ganges', 'Sarnath'],
'goa': ['Baga Beach', 'Calangute Beach', 'Dudhsagar Falls']
}

@app.get("/get_items/{name}")
async def hello(name):
    return  indian_places.get(name)





        # # Initialize variables for storing predictions
        # predictions = []

        # # Process the CSV file in chunks
        # chunk_size = 1  # Adjust as needed
        # for chunk in pd.read_csv("train.csv", chunksize=chunk_size):
        #     # Prepare the data
        #     y_true = chunk[TARGET_COLUMN]
        #     y_true.replace(TargetValueMapping().to_dict(), inplace=True)
        #     chunk.drop(TARGET_COLUMN, axis=1, inplace=True)

        #     # Load the model and make predictions
        #     model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        #     if not model_resolver.is_model_exits():
        #         return Response("Model is not available", status_code=404)

        #     best_model_path = model_resolver.get_best_model_path()
        #     model: SensorModel = load_object(file_path=best_model_path)
        #     y_pred = model.predict(chunk)

        #     # Add predictions to the DataFrame
        #     chunk['predicted_column'] = y_pred
        #     chunk['predicted_column'].replace(TargetValueMapping().reverse_mapping(), inplace=True)

        #     # Append predictions to the list
        #     predictions.append(chunk)

        # # Concatenate all chunks into a single DataFrame
        # result_df = pd.concat(predictions)

        # # Convert the DataFrame to JSON and return as a response
        # result = result_df.to_json(orient="records")
        # return Response(content=result, media_type="application/json")





