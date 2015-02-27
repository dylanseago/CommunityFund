git pull
git add * -f -A

MSG='.'

if [ $? -ne 1]; then
	MSG=$1
fi

git commit -m '$MSG'
git push

