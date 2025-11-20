PYTHONPATH=. pytest
=========================================================================================================== test session starts ============================================================================================================
platform linux -- Python 3.10.12, pytest-9.0.1, pluggy-1.6.0
rootdir: /home/sebastien/Developpement/Simplon/OPCO-ATLAS-Module-1-Brief-2
plugins: Faker-37.3.0, anyio-4.11.0
collected 2 items

tests/test_api.py ..                                                                                                                                                                                                                 [100%]

============================================================================================================= warnings summary =============================================================================================================
tests/test_api.py::test_predict
  /home/sebastien/Developpement/Simplon/OPCO-ATLAS-Module-1-Brief-2/predict_api.py:67: PydanticDeprecatedSince20: The `dict` method is deprecated; use `model_dump` instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.11/migration/
    df = pd.DataFrame([input_data.dict()])

tests/test_api.py::test_predict
  /home/sebastien/.local/lib/python3.10/site-packages/tensorflow/python/framework/ops.py:315: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
    return float(self._numpy())

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================================================================================================== 2 passed, 2 warnings in 2.87s =======================================================================================================
