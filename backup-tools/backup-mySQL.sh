##
# Backup do MySQL
# @author Augusto Morais <aflavio at gmail.com>
##

declare DATA=`date +%Y%m%d`
declare DIR_BACKUP=/home/aflavio/backups/mysql/
declare NOME=backup_geral_mySQL-in-$DATA.sql
declare SENHA=G1rEonBm8rXOzdXNkJeP

mkdir $DIR_BACKUP/$DATA

DIR_BACKUP=$DIR_BACKUP$DATA

echo .MYSQL.

echo .Iniciando backup do banco de dados.

#Executa o backup de todo banco de dados
mysqldump -u root -p$SENHA --all-databases > $DIR_BACKUP/$NOME

if [ $? -eq 0 ]; then
echo .Backup geral do Banco de dados completo.
else
echo .ERRO ao realizar o Backup geral do Banco de dados.
fi

#Backup por partes
BANCOS=$(mysql -u root -p$SENHA -e 'show databases')

#retira palavra database
#BANCOS=${BANCOS:9:${#BANCOS}}

declare CONT=0
for banco in $BANCOS
do
if [ $CONT -ne 0 ]; then
NOME=backup_my_$banco_$DATA.sql

echo -e ".Iniciando backup do banco de dados: [$banco]:"

mysqldump -u root -p$SENHA --databases $banco > $DIR_BACKUP/$NOME

if [ $? -eq 0 ]; then
echo -e ".Backup Banco de dados [$banco] completo"
else
echo "ERRO ao realizar o Backup do Banco de dados [$banco]."
fi

fi

CONT=$(($CONT+1))
done
echo -e ".Compactando Backup"
cd $DIR_BACKUP
tar -zcvf backup_geral_mySQL-in-$DATA.sql.tar.gz backup_geral_mySQL-in-$DATA.sql
rm -rf $NOME  backup_geral_mySQL-in-$DATA.sql
chown aflavio:aflavio $DIR_BACKUP -R
