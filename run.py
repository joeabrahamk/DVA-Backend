from app import create_app

app = create_app()

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the app: {e}")
