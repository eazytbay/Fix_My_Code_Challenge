###
#
#  Integer arguments sorted in ascending order
#
###

rslt = []
ARGV.each do |arg|
    # if not integer, skip
    next if arg !~ /^-?[0-9]+$/

    # conversion to integer
    i_arg = arg.to_i

    # insert result at the right position
    is_inserted = false
    x = 0
    y = rslt.size
    while !is_inserted && x < y do
        if rslt[x] < i_arg
            x += 1
        else
            rslt.insert(x, i_arg)
            is_inserted = true
            break
        end
    end
    rslt << i_arg if !is_inserted
end

puts rslt
