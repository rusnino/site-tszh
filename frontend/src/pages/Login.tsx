const Login = () => {
  return (
    <div className="card" style={{ maxWidth: "420px" }}>
      <h1>Вход</h1>
      <div className="grid">
        <label>
          Email
          <input className="input" type="email" placeholder="name@example.com" />
        </label>
        <label>
          Пароль
          <input className="input" type="password" placeholder="••••••••" />
        </label>
        <button className="button">Войти</button>
      </div>
    </div>
  );
};

export default Login;
