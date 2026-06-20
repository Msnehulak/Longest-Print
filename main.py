import LongestPrint
import CreateReadMe

lp = LongestPrint.LongestPrint()
lp.main()
lp.print_data()

data = lp.get_data()
rmb = CreateReadMe.CreateReadMe(data)
rmb.main()

