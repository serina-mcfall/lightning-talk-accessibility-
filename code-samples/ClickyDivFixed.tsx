function ClickyDivFixed() {
  const handleClick = () => alert('clicked')

  return (
    <div
      role="button"
      tabIndex={0}
      onClick={handleClick}
      onKeyDown={(e) =>
        (e.key === 'Enter' || e.key === ' ') && handleClick()
      }
    >
      Click me
    </div>
  )
}

export default ClickyDivFixed
