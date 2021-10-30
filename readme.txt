Heaploop:
Number of instruction pages: 7
Number of data pages: 135
Page most accessed from instruction pages: 0x108
Page most accessed from data pages: 0x1fff000

The pages that are accessed the most are 0x108 and 0x1fff000. The page 0x1fff000 is accessed the most because it is present in the trf files
in various forms such as 0x1fff00082e, 0x1fff00081c and 0x1fff000930. Although they are different, the vpn (last 3 digits) must be removed
and that homogenizes the rest of the address leading it to have an abnormally high amount of times its been accessed. It reflects the
number of times a local variable is stored (mainly through the use of loops in the page). The 0x108 refers to a constant, this is likely
due to the variables of MARKER_START, MARKER_END, 500 in the heap_loop call and RECORD SIZE. It frequents constants thus causing it to
create a large page that refers to constants.

Matmul:
Number of instruction pages: 10
Number of data pages: 397
Page most accessed from instruction pages: 0x108
Page most accessed from data pages: 0x1fff000

The pages that are accessed the most are 0x108 and 0x1fff000. The page 0x1fff000 is accessed the most because it is present in the trf files
in various forms such as 0x1fff00082e, 0x1fff00081c and 0x1fff000930. Although they are different, the vpn (last 3 digits) must be removed
and that homogenizes the rest of the address leading it to have an abnormally high amount of times its been accessed. It reflects the
number of times a local variable is stored (mainly through the use of loops in the page). The 0x108 refers to a constant, this is likely
due to the variables of MARKER_START, MARKER_END and PAD. It frequents constants thus causing it to create a large page that refers to 
constants. Although it does not seem like this should be the case for matmul as well, the program I have developed results in the same 
outcome as heaploop. My hypothesis was that it would be a page relating to the loops as they are frequently used and take up most of the
memory in the file matmul.c
