# pythonnotpowerpoint

## Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/brummiesteven/pythonnotpowerpoint.git
   cd pythonnotpowerpoint
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Create a `requirements.txt` file and add the following dependency:
   ```bash
   Flask
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app/main.py
   ```

6. Open your web browser and navigate to `http://127.0.0.1:5000` to view the slides.

## Using the Slide Generation Feature

1. Create your slides in the `app/templates` directory. Each slide should be an HTML file.

2. Add your slides to the `slides` list in `app/main.py`.

3. Start the application and navigate through the slides by clicking the "Next" button on the webpage.
