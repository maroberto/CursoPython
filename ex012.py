nome = 'marcos'


cores = {'branco'    :'\033[1:29m',
         'vermelho'  :'\033[1:31m',
         'verde'     :'\033[1:32m',
         'amarelo'   :'\033[1:33m',
         'azul'      :'\033[1:34m',
         'ambar'     :'\033[1:35m',
         'azul_claro':'\033[1:36m',
         'cinza'     :'\033[1:37m'}


print(('{} {}'.format(cores['branco'], nome)))
