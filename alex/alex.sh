
function alex()
{
	function push()
	{
		echo $PWD > $alex_dir/pushpop.txt
	}

	function pop()
	{
		while read line; do mydir="$line"; done < $alex_dir/pushpop.txt
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
		python $alex_dir/main.py $@
	fi
}