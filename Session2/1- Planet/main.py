import argparse
import os
import requests
import fal
import dotenv

dotenv.load_dotenv(".env")


def generate_image_from_user_input(plant_name):

    handler = fal.apps.submit(
        "fal-ai/fast-sdxl",
        path="/image-to-image",
        arguments={
            "image_url": "https://www.ikea.com/gb/en/images/products/fejka-artificial-potted-plant-with-pot-in-outdoor-succulent__0614211_pe686835_s5.jpg?f=xxl",
            "prompt": f"an image of {plant_name} plant"
        },
    )
    for event in handler.iter_events():
        if isinstance(event, fal.apps.InProgress):
            print('Request in progress ...')
    result = handler.get()
    return result


def get_name_from_generated_image(result):
    image_url = result.get("images")[0].get("url")

    PLANT_NET_API_KEY = os.getenv("PLANTNET_API_KEY")
    PROJECT = "all"  # try specific floras: "weurope", "canada"…
    print(f"Processing image to text for {image_url}")
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={PLANT_NET_API_KEY}&images={image_url}"

    data = {'organs': ['auto']}
    try:
        response = requests.get(api_endpoint, json=data, headers={'Content-Type': 'application/json'})
        response_data = response.json()
        final_name = response_data.get("bestMatch")
        return final_name
    except Exception as e:
        print("Something went wrong during request to plantnet")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='TextImageText')
    parser.add_argument('name')
    args = parser.parse_args()

    result = generate_image_from_user_input(args.name)
    flower_name = get_name_from_generated_image(result)

    if not flower_name:
        print("Try one more time, Generated image might be not realistic ...")
    else:
        print(flower_name)