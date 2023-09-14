select s.stock_name,sum(case 
                      when s.operation='buy' then -s.price
                      when s.operation='sell' then s.price
                     end) as capital_gain_loss
from Stocks s
group by s.stock_name