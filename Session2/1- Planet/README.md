# Text-to-Image-to-Text Script

This script takes the name of a flower as input, generates an image of that flower using the FAL library, and then uses
the PlantNet API to convert the generated image back to the name of the flower.

## Usage

1. Install the required dependencies:

    ```
    pip install requests fal python-dotenv
    ```
2. Create a `.env` file in the project directory and add your PlantNet API key:

    ```
   FAL_AI_KEY=<FAL_AI_KEY>
   PLANTNET_API_KEY=<PLANTNET_API_KEY>
    ```

4. Run the script:

    ```
    python script.py <flower_name>
    ```

   Replace `<flower_name>` with the name of the flower you want to convert.

5. The script will generate an image of the specified flower, process it using the PlantNet API, and print the name of
   the flower.

## Example

Suppose you want to convert the name of the flower "rose" to an image and then back to text. Run the script as follows:

```bash
python main.py rose
```