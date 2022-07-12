class Survey():
    def __init__(self):
        from easywm.cli.questions import af_server, af_wm, af_term, af_los, af_confirm
        import easywm.misc.variables as var

        while True:
            while var.current_question == 1:
                self.server = af_server()

            while var.current_question == 2:
                self.wm = af_wm(self.server)

            while var.current_question == 3:
                self.term = af_term(self.server)

            while var.current_question == 4:
                self.los = af_los()

            while var.current_question == 5:
                confirm = af_confirm(self.server, self.wm, self.term, self.los)

            if confirm:
                break
            elif var.current_question > 5:
                var.current_question = 1
