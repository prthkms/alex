function push()
{
	echo $PWD > pushpop.txt #replace with path to pushpop.txt
}

function pop()
{
	while read line; do mydir="$line"; done <pushpop.txt #replace with path to pushpop.txt
	cd $mydir
}

if [ $1 = "push" ]
then
	push
elif [ $1 = "pop" ]
then
	pop
else
	varargs=$@
	export varargs
	./t2.sh #to be replaced by alex, which calls main.py
fi
