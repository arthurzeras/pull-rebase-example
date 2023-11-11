class Integration:
    def __configure_params(self):
        print('config params')

    def cloud_integrations(self, cloud):
        if cloud == 'azure':
            self.azure_integration()

        print('cloud integrations')

    def azure_integration(self):
        print('azure integration')
        self.__configure_params()

    def aws_integration():
        print('aws integration')
