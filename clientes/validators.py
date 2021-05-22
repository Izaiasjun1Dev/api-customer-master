import re
from validate_docbr import CPF


def cpf_valido(cpf):
    valid_cpf = CPF()
    return valid_cpf.validate(cpf)


def validate_nome(nome):
    return nome.isalpha()


def validate_rg(rg):
    return len(rg) == 9


def validate_celular(celular):
    """Verifica se um celular é valido!"""
    mode = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    res = re.findall(mode, celular)

    return res
