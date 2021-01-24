import pytest
from azuremlutils import AzureRunLogCallback

class FakeRecorder():
    metric_names = ['a','epoch','time','mydict']
    log = [1,2,3,{'b':4,'c':5}]

class FakeLearner():
    recorder = FakeRecorder()

class FakeRunContext():
    output = []
    def log(self, name, value):
        self.output.append(f'{name}={value}')

def test_callback():
    fake_run_context = FakeRunContext()
    cb = AzureRunLogCallback(fake_run_context)
    cb.learn = FakeLearner()
    cb.after_epoch()
    assert fake_run_context.output == ['a=1','mydict_b=4','mydict_c=5']
    