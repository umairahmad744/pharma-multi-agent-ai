from fastapi import FastAPI

from graphs.workflow import graph
from models.request_models import QueryRequest
from fastapi.middleware.cors import CORSMiddleware
from logger import logger
from fastapi import HTTPException
from fastapi.responses import FileResponse

from utils.pdf_generator import generate_pdf

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


@app.get("/")
def home():

    return {
        "message": "Pharma AI System Running"
    }


@app.post("/ask")
def ask_ai(data: QueryRequest):

    try:

        if not data.query.strip():

            raise HTTPException(

                status_code=400,

                detail="Query cannot be empty"

            )


        logger.info(f"Query received: {data.query}")


        result = graph.invoke(

            {

                "query": data.query

            }

        )


        logger.info("Request completed successfully")


        return result


    except HTTPException:

        raise


    except Exception as e:

        logger.error(f"System error: {str(e)}")


        raise HTTPException(

            status_code=500,

            detail="Internal server error"

        )
        
@app.post("/download-report")

def download_report(data: QueryRequest):

    result=graph.invoke(

        {

            "query":data.query

        }

    )


    filename=generate_pdf(result)


    return FileResponse(

        filename,

        media_type="application/pdf",

        filename=filename

    )