class bank_account:
    def __init__(self, number_account, name_account, type_account,
                 surplus, name_bank, release_date, expiration_date):
        self.number_account = number_account
        self.set_name_account(name_account)
        self.name_account = self.last_name + " " + self.mid_name + self.first_name
        self.type_account = type_account
        self.surplus = surplus
        self.name_bank = name_bank
        self.release_date = release_date
        self.expiration_date = expiration_date

    def set_name_account(self, name_account: str):
        words = name_account.split(" ")
        self.first_name = words[len(words) - 1]
        self.last_name = words[0]
        self.mid_name = ""
        for i in range(1, len(words) - 1):
            self.mid_name += words[i] + ' '
