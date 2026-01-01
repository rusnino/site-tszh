const AdminDashboard = () => {
  return (
    <div className="grid">
      <section className="card">
        <h1>Административная панель</h1>
        <p>Контроль заявок, пользователей и показателей SLA.</p>
      </section>
      <section className="grid grid-3">
        <div className="card">
          <h3>Новые заявки</h3>
          <p>14</p>
        </div>
        <div className="card">
          <h3>В работе</h3>
          <p>32</p>
        </div>
        <div className="card">
          <h3>Просрочены</h3>
          <p>3</p>
        </div>
      </section>
    </div>
  );
};

export default AdminDashboard;
