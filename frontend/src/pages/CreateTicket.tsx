const CreateTicket = () => {
  return (
    <div className="card" style={{ maxWidth: "640px" }}>
      <h1>Новая заявка</h1>
      <div className="grid">
        <label>
          Тема
          <input className="input" type="text" placeholder="Протечка в ванной" />
        </label>
        <label>
          Описание
          <textarea className="textarea" rows={4} placeholder="Опишите проблему" />
        </label>
        <label>
          Категория
          <select className="select">
            <option>Сантехника</option>
            <option>Электрика</option>
            <option>Лифт</option>
            <option>Благоустройство</option>
          </select>
        </label>
        <label>
          Приоритет
          <select className="select">
            <option>Высокий</option>
            <option>Средний</option>
            <option>Низкий</option>
          </select>
        </label>
        <button className="button">Отправить</button>
      </div>
    </div>
  );
};

export default CreateTicket;
