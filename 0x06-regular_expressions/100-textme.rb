#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?\S+)\].*\[to:(\+?\d+)\].*\[flags:([-?0-9:]+)\]/).join(',')
