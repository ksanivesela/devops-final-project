from flask import Flask, request, jsonify
from flask_cors import CORS

from database import db, DATABASE_URL
from models import User

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return jsonify({
        "message": "Backend funcionando correctamente"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return jsonify([
        user.to_dict()
        for user in users
    ])


@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:

        return jsonify({
            "error": "Todos los campos son obligatorios"
        }), 400

    existe = User.query.filter_by(
        correo=correo
    ).first()

    if existe:

        return jsonify({
            "error": "El correo ya existe"
        }), 400

    nuevo = User(
        nombre=nombre,
        correo=correo
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({
        "message": "Usuario creado correctamente"
    }), 201


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    user = User.query.get(id)

    if not user:

        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "Usuario eliminado"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )