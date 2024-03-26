# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_build_classifier.py

DESCRIPTION:
    This sample demonstrates how to build a classifier model. For this sample, you can use the training
    documents found in https://aka.ms/azsdk/formrecognizer/sampleclassifierfiles

    More details on building a classifier and labeling your data can be found here:
    https://aka.ms/azsdk/formrecognizer/buildclassifiermodel

USAGE:
    python sample_build_classifier.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Form Recognizer resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer API key
    3) CLASSIFIER_CONTAINER_SAS_URL - The shared access signature (SAS) Url of your Azure Blob Storage container
"""
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.



import os

os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"] = "https://datasniperkpmg.cognitiveservices.azure.com"
os.environ["AZURE_FORM_RECOGNIZER_KEY"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
os.environ["CLASSIFIER_CONTAINER_SAS_URL"] = "https://rapdatasniper.blob.core.windows.net/raptestcontainer?sp=racwl&st=2024-03-26T09:41:04Z&se=2024-03-26T17:41:04Z&sv=2022-11-02&sr=c&sig=%2BofVZGuCwUdI6h3L4o%2BhBhyolbghxodHNnCNfhpBi%2Bo%3D"


def sample_build_classifier():
    # [START build_classifier]
    from azure.ai.formrecognizer import (
        DocumentModelAdministrationClient,
        ClassifierDocumentTypeDetails,
        BlobSource,
    )
    from azure.core.credentials import AzureKeyCredential

    endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]
    container_sas_url = os.environ["CLASSIFIER_CONTAINER_SAS_URL"]

    document_model_admin_client = DocumentModelAdministrationClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_model_admin_client.begin_build_document_classifier(
        doc_types={
            "Form_1.jpg": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "Form_2.jpg": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "Form_3.jpg": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "Form_4.jpg": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "Form_5.jpg": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "IRS_1040_1_01.pdf": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "IRS_1040_1_02.pdf": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "IRS_1040_1_03.pdf": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "IRS_1040_1_04.pdf": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
            "IRS_1040_1_05.pdf": ClassifierDocumentTypeDetails(
                source=BlobSource(
                    container_url=container_sas_url
                )
            ),
        },
        description="IRS document classifier live test",
    )
    result = poller.result()
    print(f"Classifier ID: {result.classifier_id}")
    print(f"API version used to build the classifier model: {result.api_version}")
    print(f"Classifier description: {result.description}")
    print(f"Document classes used for training the model:")
    for doc_type, details in result.doc_types.items():
        print(f"Document type: {doc_type}")
        print(f"Container source: {details.source.container_url}\n")
    # [END build_classifier]


if __name__ == "__main__":
    sample_build_classifier()