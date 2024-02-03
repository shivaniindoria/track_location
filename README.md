
# Phone Number Location Tracker

This Python script uses the `phonenumbers` library to get the location and carrier information of a phone number with the help of OpenCage Geocoding API. It then displays the location on a map using the Folium library.

## Requirements

- Python 3.x
- Install required libraries:
  ```
  pip install phonenumbers opencage geopy folium
  ```

## Usage

1. Run the script:
   ```
   python location_tracker.py
   ```
2. Enter the phone number (with the country code) when prompted.
3. The script will display the location and service provider information and generate an HTML map with the location.

## Configuration

- Obtain an API key from OpenCage Geocoding API: [OpenCage API Key](https://opencagedata.com/)
- Replace the `key` variable in the script with your API key.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [phonenumbers](https://pypi.org/project/phonenumbers/)
- [OpenCage Geocoding API](https://opencagedata.com/)
- [Folium](https://python-visualization.github.io/folium/)

Feel free to contribute or report issues! 🚀
