from flask import Blueprint, send_file

bp = Blueprint('download', __name__)

@bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(f'/path/to/downloads/{filename}', as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404
