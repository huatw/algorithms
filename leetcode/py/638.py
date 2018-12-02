class Solution:
    def shoppingOffers(self, prices, specials, needs):
        cache = {}

        def dfs(needs):
            if needs not in cache:
                min_cost = sum(need * price for need, price in zip(needs, prices))
                for (*offer, offer_cost) in specials:
                    if all(need >= cnt for need, cnt in zip(needs, offer)):
                        new_needs = tuple(need - cnt for need, cnt in zip(needs, offer))
                        min_cost = min(min_cost, offer_cost + dfs(new_needs))
                cache[needs] = min_cost
            return cache[needs]

        return dfs(tuple(needs))




class Solution:
    def shoppingOffers(self, prices, specials, needs):
        def with_cache(fn):
            cache = {}
            def wrapper(needs):
                if needs not in cache:
                    cache[needs] = fn(needs)
                return cache[needs]
            return wrapper

        @with_cache
        def dfs(needs):
            min_cost = sum(need * price for need, price in zip(needs, prices))
            for (*offer, offer_cost) in specials:
                if all(need >= cnt for need, cnt in zip(needs, offer)):
                    new_needs = tuple(need - cnt for need, cnt in zip(needs, offer))
                    min_cost = min(min_cost, offer_cost + dfs(new_needs))
            return min_cost

        return dfs(tuple(needs))
