const Register = () => {
  return (
    <div className="card" style={{ maxWidth: "520px" }}>
      <h1>Регистрация</h1>
      <div className="grid">
        <label>
          ФИО
          <input className="input" type="text" placeholder="Иван Иванов" />
        </label>
        <label>
          Email
          <input className="input" type="email" placeholder="name@example.com" />
        </label>
        <label>
          Пароль
          <input className="input" type="password" placeholder="••••••••" />
        </label>
        <label>
          Квартира
          <input className="input" type="text" placeholder="101" />
        </label>
        <button className="button">Создать аккаунт</button>
      </div>
    </div>
  );
};

export default Register;
