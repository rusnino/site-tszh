const AdminTicketDetails = () => {
  return (
    <div className="grid">
      <section className="card">
        <h1>Заявка #41</h1>
        <p>Житель: Иван Житель, кв. 101</p>
        <p>Статус: Новая</p>
        <p>Категория: Сантехника</p>
        <p>Приоритет: Высокий</p>
      </section>
      <section className="card">
        <h2 className="section-title">AI-помощник</h2>
        <p>
          <strong>Предложенная категория:</strong> Сантехника
        </p>
        <p>
          <strong>Предложенный приоритет:</strong> Высокий
        </p>
        <p>
          <strong>Возможные дубликаты:</strong> #12, #18
        </p>
        <p>
          <strong>Черновик ответа:</strong> Спасибо за обращение, заявка принята
          и передана мастеру.
        </p>
        <span className="badge">Требуется подтверждение диспетчера</span>
      </section>
      <section className="card">
        <h2 className="section-title">Комментарии</h2>
        <textarea className="textarea" rows={3} placeholder="Комментарий для мастера" />
        <button className="button">Сохранить</button>
      </section>
    </div>
  );
};

export default AdminTicketDetails;
