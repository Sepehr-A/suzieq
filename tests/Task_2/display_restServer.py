import os
from fastapi import FastAPI, HTTPException
from display_cli import read_file

app = FastAPI()


@app.get("/ping_results/{filename}")
async def read_ping_results(filename: str):
    try:
        base_directory = os.path.join(os.getcwd(), 'ping_results')
        table_path = os.path.join(base_directory, filename)
        print(table_path)
        ping_table = read_file(table_path)
        if ping_table.empty:
            raise HTTPException(status_code=404, detail="Ping results file is empty or not found.")

        return ping_table.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
