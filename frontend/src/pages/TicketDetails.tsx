const TicketDetails = () => {
  return (
    <div className="grid">
      <section className="card">
        <h1>Заявка #101</h1>
        <p>Статус: В работе</p>
        <p>Категория: Сантехника</p>
        <p>Срок выполнения: 24 часа</p>
      </section>
      <section className="card">
        <h2 className="section-title">Комментарии</h2>
        <div className="grid">
          <div>
            <strong>Диспетчер:</strong> Заявка принята, назначен мастер.
          </div>
          <div>
            <strong>Мастер:</strong> Осмотр запланирован на сегодня 18:00.
          </div>
        </div>
      </section>
      <section className="card">
        <h2 className="section-title">Добавить комментарий</h2>
        <textarea className="textarea" rows={3} placeholder="Ваше сообщение" />
        <button className="button">Отправить</button>
      </section>
    </div>
  );
};

export default TicketDetails;
