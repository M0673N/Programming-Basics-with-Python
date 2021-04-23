campaign_days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
cake_price = 45
waffles_price = 5.8
pancakes_price = 3.2
print((campaign_days * bakers * cakes * cake_price + campaign_days * bakers * waffles * waffles_price + campaign_days
       * bakers * pancakes * pancakes_price) - (campaign_days * bakers * cakes * cake_price + campaign_days * bakers
                                                * waffles * waffles_price + campaign_days * bakers * pancakes
                                                * pancakes_price) / 8)
