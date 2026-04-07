import sender_stand_request
import data

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_name):
    response = sender_stand_request.post_new_client_kit(kit_name, get_new_user_token())
    assert response.status_code == 201

def negative_assert(kit_name):
    response = sender_stand_request.post_new_client_kit(kit_name, get_new_user_token())
    assert response.status_code == 400


def test_1_nombre_del_kit_con_una_letra():
    current_body = get_kit_body("A")
    positive_assert(current_body)

def test_2_nombre_del_kit_con_511_letras():
    current_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(current_body)

def test_3_kit_sin_nombre():
    current_body = get_kit_body("")
    negative_assert(current_body)

def test_4_kit_con_mas_de_512_letras_no_permitidas():
    current_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(current_body)

def test_5_nombre_del_kit_con_caracteres_especiales():
    current_body = get_kit_body("№%@")
    positive_assert(current_body)

def test_6_kit_se_permiten_espacios_en_el_nombre():
    current_body = get_kit_body(" A Aaa ")
    positive_assert(current_body)

def test_7_se_permiten_numeros_en_el_nombre():
    current_body = get_kit_body("123")
    positive_assert(current_body)

def test_8_el_parametro_no_se_pasa_en_la_solicitud():
    current_body = get_kit_body()
    negative_assert(current_body)

def test_9_parametro_diferente_en_numero():
    current_body = get_kit_body(123)
    negative_assert(current_body)

