#[cfg(feature = "python-extension")]
use pyo3::prelude::*;

#[cfg(feature = "python-extension")]
mod utils;
#[cfg(feature = "python-extension")]
use utils::generate_password;

#[cfg(feature = "python-extension")]
#[pyfunction]
fn generate_password_py(length: usize, password_type: &str) -> PyResult<String> {
    Ok(generate_password(length, password_type))
}

#[cfg(feature = "python-extension")]
#[pymodule]
fn pwdgen(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_password_py, m)?)?;

    Ok(())
}
